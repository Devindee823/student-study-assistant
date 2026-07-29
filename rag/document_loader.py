from langchain_community.document_loaders import PyPDFLoader
import os


def load_documents(folder):

    documents = []

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            path = os.path.join(folder, file)

            loader = PyPDFLoader(path)

            documents.extend(loader.load())

    return documents


from langchain_community.document_loaders import PyPDFLoader
import os


def load_documents(folder):

    documents = []

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            path = os.path.join(folder, file)

            loader = PyPDFLoader(path)

            documents.extend(loader.load())

    return documents
