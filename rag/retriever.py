from rag.vector_store import load_vector_store


def get_retriever():
    vectorstore = load_vector_store()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


def retrieve_documents(question):
    retriever = get_retriever()

    documents = retriever.invoke(question)

    seen = set()
    cleaned_docs = []

    for doc in documents:
        text = doc.page_content.strip()

        if text not in seen:
            cleaned_docs.append(text)
            seen.add(text)

    context = "\n\n".join(cleaned_docs)

    return context