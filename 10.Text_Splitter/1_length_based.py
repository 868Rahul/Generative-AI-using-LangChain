from langchain_community.document_loaders import PyPDFLoader

try:
    from langchain_text_splitters import CharacterTextSplitter
except ImportError:
    from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator=''
)

texts = splitter.split_documents(docs)

print(f'Number of chunks: {len(texts)}')
print(texts[0].page_content)
print(texts[1].page_content)
