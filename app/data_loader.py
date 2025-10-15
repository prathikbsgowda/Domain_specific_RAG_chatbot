import os
from PyPDF2 import PdfReader
from langchain.docstore.document import Document
from app.config import DATA_FOLDER

def load_documents():
    docs = []
    if not os.path.exists(DATA_FOLDER):
        print(f"⚠️ Folder '{DATA_FOLDER}' not found.")
        return docs

    for file in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, file)
        if file.endswith(".pdf"):
            try:
                pdf = PdfReader(path)
                text = "".join(page.extract_text() or "" for page in pdf.pages)
                if text.strip():
                    docs.append(Document(page_content=text, metadata={"source": file}))
            except Exception as e:
                print(f"Error reading {file}: {e}")
        elif file.endswith(".txt"):
            print(file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                if text.strip():
                    docs.append(Document(page_content=text, metadata={"source": file}))
            except Exception as e:
                print(f"Error reading {file}: {e}")
    return docs
