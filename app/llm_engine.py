from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from app.config import LLM_MODEL

def load_llm():
    print("🔹 Loading LLM model (Flan-T5-base)...")
    gen_pipeline = pipeline("text2text-generation", model=LLM_MODEL, max_new_tokens=256)
    return HuggingFacePipeline(pipeline=gen_pipeline)

def rewrite_query(llm, query: str) -> str:
    replacements = {
        "explain": "what is",
        "describe": "what is",
        "define": "what is",
        "tell me about": "what is",
        "give information about": "what is",
        "can you explain": "what is",
    }

    q_lower = query.lower()
    for old, new in replacements.items():
        if old in q_lower:
            q_lower = q_lower.replace(old, new)
    normalized_query = q_lower.strip()

    prompt = (
        f"Rephrase the following user question into a concise factual query for a retrieval system.\n\n"
        f"User question: '{normalized_query}'\n"
        f"Output only the rewritten question, without extra text or explanation."
    )

    try:
        rewritten = llm.invoke(prompt).strip()
        if not rewritten:
            rewritten = normalized_query
    except Exception:
        rewritten = normalized_query

    return rewritten

