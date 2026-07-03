import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)
# prompt 1 - report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
# prompt 2 - summary
template2 = PromptTemplate(
    template='Write a 5 lines summary on the following text: \n {text}',
    input_variables=["text"]
)

prompt1 = template1.invoke({'topic': 'Black Holes'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})
result1 = model.invoke(prompt2)

print(f"Report on Black Holes:\n{result.content}\n")
print(f"Summary of the report:\n{result1.content}\n")