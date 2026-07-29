from rag.retriever import retrieve_documents
from models.llm import get_llm


def study_agent(question):

    context = retrieve_documents(question)

    if not context:
        return "I could not find relevant information from the study documents."

    llm = get_llm()

    prompt = f"""
You are a helpful student study assistant.

Use the following study document to answer the question.

Question:
{question}

Study Document:
{context}

Give a complete answer.
Include:
- Disease names
- Affected fish species
- Symptoms
- Short explanation

Answer in simple student-friendly language.
"""

    response = llm(prompt)

    return response