from dotenv import load_dotenv
from typing import Literal

from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    PydanticOutputParser,
)
from langchain_core.runnables import (
    RunnableBranch,
    RunnablePassthrough,
)

load_dotenv()

# ---------------- Model ----------------

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

str_parser = StrOutputParser()

# ---------------- Pydantic Model ----------------

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback"
    )

parser = PydanticOutputParser(pydantic_object=Feedback)

# ---------------- Classification Prompt ----------------

classifier_prompt = PromptTemplate(
    template="""
Classify the sentiment of the following feedback as either
'positive' or 'negative'.

Feedback:
{feedback}

{format_instructions}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

classifier_chain = classifier_prompt | model | parser

# ---------------- Response Prompts ----------------

positive_prompt = PromptTemplate(
    template="""
Write a polite response to this positive feedback:

{feedback}
""",
    input_variables=["feedback"],
)

negative_prompt = PromptTemplate(
    template="""
Write a polite response to this negative feedback:

{feedback}
""",
    input_variables=["feedback"],
)

# ---------------- Preserve Original Input ----------------

prepare_input = RunnablePassthrough.assign(
    sentiment=classifier_chain
)

# ---------------- Conditional Branch ----------------

branch_chain = RunnableBranch(
    (
        lambda x: x["sentiment"].sentiment == "positive",
        positive_prompt | model | str_parser,
    ),
    (
        lambda x: x["sentiment"].sentiment == "negative",
        negative_prompt | model | str_parser,
    ),
    lambda x: "Could not determine sentiment.",
)

# ---------------- Final Chain ----------------

chain = prepare_input | branch_chain

# ---------------- Run ----------------

result = chain.invoke(
    {
        "feedback": "This is a wonderful phone."
    }
)

print(result)

# Optional
chain.get_graph().print_ascii()