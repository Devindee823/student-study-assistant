from langchain_chroma import Chroma
from rag.embeddings import get_embeddings

PERSIST_DIRECTORY = "chroma_db"


def create_vector_store(documents):
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    return vectorstore


def load_vector_store():
    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    return vectorstore