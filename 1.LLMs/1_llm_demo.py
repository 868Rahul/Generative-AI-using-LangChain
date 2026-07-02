
from dotenv import load_dotenv

load_dotenv()

# LangChain LLM Demo Using OpenAI

# from langchain_openai import OpenAI
#
# llm = OpenAI(
#     model="gpt-3.5-turbo-instruct"
# )
#
# # LLM takes a string as input and returns a string
# result = llm.invoke("What is the capital of India?")
# print(result)



# LangChain LLM Demo Using OpenAI & Gemini (Same File)

from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash"
)

# LLM takes a string as input and returns a string
result = llm.invoke("What is the capital of India?")
print(result)