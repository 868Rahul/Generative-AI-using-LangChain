from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

chatModel = ChatAnthropic(model="claude-2", temperature=0.7, max_tokens=1000)
result = chatModel.invoke("What is the capital of India?")
print(result.content)