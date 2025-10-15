from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from app.config import LLM_MODEL

def load_llm():
    print("🔹 Loading LLM model (Flan-T5-base)...")
    gen_pipeline = pipeline("text2text-generation", model=LLM_MODEL, max_new_tokens=256)
    return HuggingFacePipeline(pipeline=gen_pipeline)

def rewrite_query(llm, query):
    """Rewrites user query for better retrieval"""
    prompt = f"Rewrite this question for better information retrieval:\n{query}"
    rewritten = llm(prompt).strip()
    return rewritten if rewritten else query
