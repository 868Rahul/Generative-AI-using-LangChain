from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = PromptTemplate(
    input_variables=["poem"],
    template="Write a summary for the following poem in five sentence. - \n{poem}"
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()
# print(len(docs))
# print(type(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem": docs[0].page_content}))