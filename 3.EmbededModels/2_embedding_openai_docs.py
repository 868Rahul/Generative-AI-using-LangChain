from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimension=32
)
docs = [
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo.",
    "The capital of India is New Delhi."]

result = embeddings.embed_documents(docs)
print(str(result))
print("Embedding length:", len(result))