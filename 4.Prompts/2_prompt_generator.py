from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""You are an expert AI assistant that summarizes academic research papers.

Summarize the research paper titled "{paper_title}" following these rules:

1. **Explanation Style:** {style_input}  
2. **Summary Length:** {length_input}  

### Content Requirements:
- Include the main goals, contributions, and key findings of the paper.
- If mathematical equations are present in the paper, include them and briefly explain them.
- Where possible, explain concepts using simple, intuitive code snippets.
- Use analogies to make complex ideas easier to understand.
- If certain specific details are unavailable, state: "This detail is not available in the provided paper" — do not leave the section empty.
- Ensure the explanation is clear, logically structured, and factually correct.

### Output Format:
- **Title**
- **Summary**
- **Key Points**
- **Mathematical/Technical Details**
- **Analogies/Examples**
""",
    input_variables=["paper_title", "style_input", "length_input"],
    validate_template=True
)


template.save('template.json')