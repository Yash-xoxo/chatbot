import openai

openai.api_key = 'your-api-key'

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

# Chatbot interaction loop
print("AI Chatbot ready! Type 'quit' to exit.")
chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    # Add user input to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Generate a response
    response = generate_response(chat_history)

    # Add bot response to chat history
    chat_history.append({"role": "assistant", "content": response})

    print(f"Bot: {response}")

