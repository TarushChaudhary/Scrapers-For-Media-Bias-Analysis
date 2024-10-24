from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM



def chat_with_llm(text,article):
    model = OllamaLLM(model="llama3.1")

    template = """
    You will be provided with a news article. Your task is to perform all instructions given below.
    Here is the news article:
    {article}
    Here are the instructions:
    {template_text}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm_chain = prompt | model
    return llm_chain.invoke({"template_text": text,"article":article})

