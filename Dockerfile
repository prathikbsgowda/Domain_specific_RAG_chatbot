# Dockerfile
FROM python:3.10-slim

WORKDIR /rag_qa_system

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-mpnet-base-v2')"

# Expose ports (FastAPI:8000, Streamlit:8501)
EXPOSE 8000
EXPOSE 8501

# Run both FastAPI and Streamlit together
CMD ["bash", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/streamlit_app.py --server.port=8501 --server.address=0.0.0.0"]
