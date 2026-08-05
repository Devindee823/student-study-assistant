# Student Study Assistant

## Project Description

The Student Study Assistant is an AI-powered learning application developed to help students study more effectively using their own learning materials. Instead of answering questions only from a language model's general knowledge, the system retrieves relevant information from uploaded documents before generating a response. This Retrieval-Augmented Generation (RAG) approach improves the accuracy and relevance of answers.

The project also uses a simple multi-agent architecture. A Planner Agent first identifies the user's request and then routes it to the appropriate agent, such as the Study Agent for explanations or the Quiz Agent for practice questions. The application is built with Streamlit to provide a simple and user-friendly interface.


## Features

* Ask questions about study materials.
* Retrieve relevant information using Retrieval-Augmented Generation (RAG).
* Multi-agent workflow for handling different types of requests.
* Interactive Streamlit web interface.
* ChromaDB vector database for document retrieval.
* Hugging Face sentence embeddings for semantic search.
* Fast and context-aware responses.



## Project Architecture


                        +----------------------+
                        |    Streamlit UI      |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |    Planner Agent     |
                        +----------+-----------+
                                   |
                +------------------+------------------+
                |                                     |
                v                                     v
         +---------------+                    +---------------+
         | Study Agent   |                    |  Quiz Agent   |
         +-------+-------+                    +---------------+
                 |
                 v
         +---------------+
         |   Retriever   |
         +-------+-------+
                 |
                 v
         +---------------+
         |   ChromaDB    |
         +-------+-------+
                 |
                 v
         +---------------+
         | Study Files   |
         +---------------+


## Agent Communication Diagram


User
 │
 ▼
Streamlit Interface
 │
 ▼
Planner Agent
 │
 ├──────────────► Quiz Agent
 │
 ▼
Study Agent
 │
 ▼
Retriever
 │
 ▼
ChromaDB
 │
 ▼
Relevant Document Chunks
 │
 ▼
AI Response
 │
 ▼
User


## RAG Pipeline

1. The user enters a question through the Streamlit application.
2. The Planner Agent identifies the type of request.
3. The Study Agent sends the query to the Retriever.
4. The Retriever searches the ChromaDB vector database.
5. The most relevant document chunks are retrieved.
6. The retrieved context is combined with the user's question.
7. The AI generates a response using the retrieved information.
8. The answer is displayed in the Streamlit interface.


## Technology Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Sentence Transformers (all-MiniLM-L6-v2)
* Git
* GitHub


## Model Choice Comparison


1. Hugging Face Embedding Model

Purpose:
- Converts study documents into vector representations.
- Enables semantic search and retrieval of relevant information from documents.

Reason for Selection:
- Lightweight and efficient.
- Provides good retrieval performance for educational documents.
- Suitable for the RAG pipeline with a large number of study materials.

 2. Large Language Model (LLM)

Purpose:
- Generates final answers using the retrieved context from the RAG pipeline.
- Provides understandable explanations for student questions.

Reason for Selection:
- Capable of understanding context.
- Produces human-like and meaningful responses.
- Helps students learn concepts more effectively.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Devindee823/student-study-assistant.git
```

### 2. Navigate to the project

```bash
cd student-study-assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Build the vector database

```bash
python test_vector.py
```

### 7. Start the application

```bash
streamlit run app.py
```


## Project Structure

student-study-assistant/
│
├── agents/
│   ├── planner_agent.py
│   ├── study_agent.py
│   └── quiz_agent.py
│
├── rag/
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── data/
├── chroma_db/
├── app.py
├── test_agent.py
├── test_rag.py
├── test_vector.py
├── requirements.txt
└── README.md



## Live Streamlit Demo

Demo URL

```
GitHub Repository Link:

https://github.com/Devindee823/student-study-assistant

Streamlit Community Cloud Live App URL:

https://devindee823-study-assistant.streamlit.app/

```

## Known Limitations

* The quality of answers depends on the uploaded study materials.
* The application can only answer questions related to indexed documents.
* Large document collections may increase retrieval time.
* Quiz generation is currently basic.
* The application does not remember previous conversations between sessions.



## Future Improvements

* Upload PDF documents directly from the web interface.
* Voice-based interaction.
* Better quiz generation with difficulty levels.
* User authentication.
* Conversation history.
* Support for additional document formats.



## Author
G.D.Harshani Devindee
ITBIN-2313-0136
