from rag.document_loader import load_documents
from rag.vector_store import create_vector_store

docs = load_documents("data/documents")
print(f"Loaded {len(docs)} documents")

vectorstore = create_vector_store(docs)

print("✅ Vector store created successfully!")