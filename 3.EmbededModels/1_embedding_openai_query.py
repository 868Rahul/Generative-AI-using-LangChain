from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimension=32
)

result = embeddings.embed_query("What is the capital of India?")
print(str(result))
print("Embedding length:", len(result))