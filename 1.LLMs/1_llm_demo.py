from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
# llm take string input and returns string output
result = llm.invoke("What is the capital of India?") 
print(result)

## LLM using Gemini
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(model="gemini-1.5-flash")
result = llm.invoke("What is the capital of India?")
print(result)
