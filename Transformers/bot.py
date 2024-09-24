from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a pretrained model and tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot interaction loop
print("AI Chatbot ready! Type 'quit' to exit.")
chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    # Add user input to chat history
    chat_history.append(user_input)

    # Join the chat history and encode it as input for the model
    input_ids = tokenizer.encode(" ".join(chat_history) + tokenizer.eos_token, return_tensors='pt')

    # Generate a response
    response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Add bot response to chat history
    chat_history.append(response)

    print(f"Bot: {response}")

