import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use "gpt-3.5-turbo" or others
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Chatbot interaction loop
print("AI Chatbot ready! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    response = generate_response(user_input)
    print(f"Bot: {response}")
