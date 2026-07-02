from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chatModel = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=1000)

result = chatModel.invoke("What is the capital of India?")
print(result.content)

