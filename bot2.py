from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a pretrained model and tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot interaction loop
print("AI Chatbot ready! Type 'quit' to exit.")
chat_history = None  # Initialize chat history

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    # Encode the user input and generate a response
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # If chat_history exists, concatenate; otherwise, start with new_input_ids
    if chat_history is not None and chat_history.numel() > 0:
        chat_history = torch.cat([chat_history, new_input_ids], dim=-1)chat_history
    else:
        chat_history = new_input_ids

    # Generate response
    response_ids = model.generate(chat_history, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(response_ids[:, chat_history.shape[-1]:][0], skip_special_tokens=True)

    print(f"Bot: {response}")
