from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

st.header("Research Paper Summarizer")

paper_input = st.selectbox(
    "Select a research paper to summarize", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Best GANs on Image Synthesis"])

style_input = st.selectbox( "Select Explanation Style", ["Simple", "Detailed", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Summary Length", ["Short - 1 or 2 paragraph ", "Medium", "Long"])

template = load_prompt('template.json')

if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        formatted_prompt = template.format(
            paper_title=paper_input,
            style_input=style_input,
            length_input=length_input
        )
        response = model.invoke(formatted_prompt)
        chain = template | model
        response = chain.invoke({
            "paper_title": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })
        st.write(response.content)
        st.success("Summary generated successfully!")
