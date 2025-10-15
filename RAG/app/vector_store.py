import os, pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from app.config import VECTOR_INDEX, EMBED_MODEL

def create_or_load_vectorstore(docs):
    if not docs:
        print("⚠️ No documents to index.")
        return None

    embedding = SentenceTransformerEmbeddings(model_name=EMBED_MODEL)

    if os.path.exists(VECTOR_INDEX):
        print("🔹 Loading existing FAISS index...")
        with open(VECTOR_INDEX, "rb") as f:
            return pickle.load(f)
    else:
        print("🔹 Creating new FAISS index...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(docs)
        vectorstore = FAISS.from_documents(chunks, embedding)
        with open(VECTOR_INDEX, "wb") as f:
            pickle.dump(vectorstore, f)
        return vectorstore
