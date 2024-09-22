import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!"]),
    (r"how are you?", ["I'm a bot, but I'm doing great! How about you?"]),
    (r"what is your name?", ["I am an AI chatbot.", "You can call me Bot!"]),
    (r"quit", ["Goodbye!"])
]

# Initialize chatbot
def chatbot():
    print("AI Chatbot ready! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
chatbot()
