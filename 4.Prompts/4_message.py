from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash")

message = [
    SystemMessage(content="You are an AI assistant"),
    HumanMessage(content="What is the capital of France?")
]
response = model.invoke(message)
message.append(AIMessage(content=response.content))
print(message)
