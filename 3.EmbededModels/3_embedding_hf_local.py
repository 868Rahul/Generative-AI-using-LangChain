from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "The capital of India is New Delhi."

# docs = [
#     "The capital of France is Paris.",
#     "The capital of Japan is Tokyo.",
#     "The capital of India is New Delhi."]
# result = embedding.embed_documents(docs)

result = embedding.embed_query(text)

# print(str(result))
print("Embedding length:", len(result))