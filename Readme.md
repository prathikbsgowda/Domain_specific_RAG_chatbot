# Domain-Specific Question Answering (RAG) System

A production-ready Retrieval-Augmented Generation (RAG) system that allows users to ask natural language questions based on uploaded documents (PDFs & text files). The system strictly responds only with information available in the provided documents and never hallucinates.

It includes a FastAPI backend, a ChatGPT-style Streamlit frontend, query rewriting, and is fully Dockerized for easy deployment.

---

##  Features

- **Strict document-based QA:** Answers come only from uploaded documents; responds with a standard message if info is missing.  
- **ChatGPT-style interface:** Modern Streamlit UI with chat bubbles, user/bot differentiation, and session history.  
- **Query rewriting:** Optimizes retrieval for more accurate responses.  
- **Greetings & small talk handling:** Responds politely to greetings like “hi”, “hello”, “good morning” with a friendly message.  
- **Persistent chat history:** All conversations are stored in `chat_history.txt`.  
- **Dynamic document ingestion:** Supports multiple PDF and TXT files for domain-specific knowledge.  
- **Dockerized:** Easy deployment anywhere (local machine, cloud, or internal network).  

---

##  Folder Structure

```
rag_qa_system/
│
├── app/
│   ├── main.py           # FastAPI backend
│   ├── config.py         # Configuration constants
│   ├── data_loader.py    # Load PDFs/TXT files
│   ├── vector_store.py   # FAISS vector database
│   ├── llm_engine.py     
│   ├── rag_pipeline.py   # RAG pipeline & strict rules
│   └── utils.py          # Utilities
│
├── frontend/
│   └── streamlit_app.py 
│
├── data/                  # Folder containing PDF/TXT documents
├── chat_history.txt       
├── requirements.txt       
└── Dockerfile             # Containerization
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository
```bash
git clone https://github.com/prathikbsgowda/Domain_specific_RAG_chatbot.git
cd rag_qa_system
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run FastAPI backend
```bash
uvicorn app.main:app --reload
```

### 4️⃣ Run Streamlit frontend
```bash
streamlit run frontend/streamlit_app.py
```

Open the UI in your browser:  
➡️ [http://localhost:8501](http://localhost:8501)

---

## 🐳 Docker Deployment

**Build Docker image:**
```bash
docker build -t rag_qa_app .
```

**Run container:**
```bash
docker run -p 8000:8000 -p 8501:8501 rag_qa_app
```

**FastAPI API:** [http://localhost:8000/docs](http://localhost:8000/docs)  
**Streamlit Chat UI:** [http://localhost:8501](http://localhost:8501)

---

##  Usage

1. Upload PDF/TXT files in the `data/` folder.  
2. Open the Streamlit chat UI.  
3. Ask questions.  
4. Bot responds **only from documents**.  
5. Greetings like “hi”, “hello”, “good morning” receive friendly responses.  
6. All Q&A are stored in `chat_history.txt`.  

**Example Queries:**

✅ “What is the company’s mission?”  
✅ “Who is the CEO?”  
💬 “Hi” → “Hello! How can I assist you today?”  
❌ “Who founded Google?” → “The answer is not available in the provided documents.”

---

##  Key Components

| Component | Purpose |
|------------|----------|
| **FastAPI** | Backend API for querying the RAG system |
| **FAISS** | Vector database for semantic retrieval |
| **SentenceTransformer** | Free embedding model for document representation |
| **Flan-T5** | Local LLM for query rewriting & response generation |
| **Streamlit** | Chat interface with user/bot message bubbles |
| **Docker** | Containerization for easy deployment |

---

##  Future Enhancements

- File upload through the UI with automatic index rebuild.  
- Source references for each answer (show which document the answer came from).  
- Small talk responses (e.g., “How are you?”).  
- Multi-language support.  
- Dashboard for evaluation metrics (accuracy, retrieval precision).  

---




