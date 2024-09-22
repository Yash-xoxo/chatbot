from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('SimpleBot')

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus
trainer.train('chatterbot.corpus.english')

# Loop to get input from the user and respond
print("Chatbot is ready! Type 'quit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print(f"Bot: {response}")
