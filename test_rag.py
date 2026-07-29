from rag.document_loader import load_documents


docs = load_documents("data/documents")


print("Documents loaded:", len(docs))


if len(docs) > 0:
    print(docs[0].page_content[:500])