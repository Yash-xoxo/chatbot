import dialogflow_v2 as dialogflow
import os

# Set your Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_key.json"

# Detect Intent from Text
def detect_intent_texts(project_id, session_id, text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code='en')
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text

# Example usage
project_id = 'your-project-id'
session_id = 'some-session-id'

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = detect_intent_texts(project_id, session_id, user_input)
    print(f"Bot: {response}")
