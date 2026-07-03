from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# chat_template = ChatPromptTemplate.from_messages(
chat_template = ChatPromptTemplate(
    [
        ('system', "You are a helpful {domain} expert."),
        ('human', "Explain in simple terms, what is {topic}")   
    ]
)

prompt = chat_template.invoke({
    'domain' : 'cricket', 'topic': 'batting average'
})
print(prompt)
