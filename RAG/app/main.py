from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.data_loader import load_documents
from app.vector_store import create_or_load_vectorstore
from app.llm_engine import load_llm
from app.rag_pipeline import answer_query

app = FastAPI(title="Domain-Specific RAG QA System (Strict Mode)")

docs = load_documents()
vectorstore = create_or_load_vectorstore(docs)
llm = load_llm()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "RAG QA System is running!"}

@app.post("/ask")
def ask_question(req: QueryRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    try:
        answer = answer_query(req.question, vectorstore, llm)
        return {"question": req.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
