from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age, and city of a fictional person \n {format_instructions}',
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.format()
result = model.invoke(prompt)
parsed_result = parser.parse(result.content)
print(parsed_result) 
print(type(parsed_result)) # <class 'dict'> python treat json object as dict.

# Instead of invoking the model directly, we can use a chain to handle the parsing automatically.
# This is a more general approach that can be used with any model and parser.
chain = template | model | parser
result = chain.invoke({})
print(result['name'])  # This will print the parsed JSON output as a dictionary

# limitations of json output parser:
#  it does not give you json object based on json schema.
