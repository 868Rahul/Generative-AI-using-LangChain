## ChatModel using Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
import os
api_key = os.getenv("GEMINI_API_KEY")

chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.6
)
result = chat.invoke("What is the capital of India?")
print(result.content)