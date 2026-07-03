from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    model_response = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": model_response.content})
    print(f"AI: {model_response.content}")

print("Chat history:")
for message in chat_history:
    print(f"{message['role'].capitalize()}: {message['content']}")