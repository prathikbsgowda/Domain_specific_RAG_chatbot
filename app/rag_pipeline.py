# app/rag_pipeline.py
from app.utils import save_chat_history
from app.llm_engine import rewrite_query

def check_greeting(query: str):
    q = query.lower().strip()
    if "good morning" in q:
        return "🌅 Good morning! How can I assist you today?"
    elif "good afternoon" in q:
        return "🌞 Good afternoon! How can I assist you today?"
    elif "good evening" in q:
        return "🌇 Good evening! How can I assist you today?"
    elif q in {"hi", "hello", "hey", "hai", "hii"}:
        return "👋 Hello! How can I assist you today?"
    return None

# def answer_query(query, vectorstore, llm):
#     # 1️⃣ Check for greetings first
#     greeting_response = check_greeting(query)
#     if greeting_response:
#         save_chat_history(query, greeting_response)
#         return greeting_response
#     better_query = rewrite_query(llm, query)
#     retriever = vectorstore.as_retriever(search_kwargs={"k": 7})
#     docs = retriever.get_relevant_documents(better_query)
#     if not docs:
#         answer = "⚠️ The answer is not available in the provided documents."
#         save_chat_history(query, answer)
#         return answer
#     context = "\n".join([d.page_content for d in docs])
#     prompt = f"""
# You are a strict assistant. Use ONLY the information in the context below.
# If the answer is not found in the context, respond exactly with:
# "The answer is not available in the provided documents."

# Context:
# {context}

# Question: {query}
# Answer:
#     """.strip()

#     answer = llm(prompt).strip()

#     # 5️⃣ Ensure no hallucinations
#     if not answer or "not available" in answer.lower() or "i don't know" in answer.lower():
#         answer = "⚠️ The answer is not available in the provided documents."

#     save_chat_history(query, answer)
#     return answer



def answer_query(query, vectorstore, llm):
    greeting_response = check_greeting(query)
    if greeting_response:
        save_chat_history(query, greeting_response)
        return greeting_response

    better_query = rewrite_query(llm, f"Make this question more specific and clear: {query}")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    docs = retriever.get_relevant_documents(better_query)

    if not docs:
        answer = "⚠️ The answer is not available in the provided documents."
        save_chat_history(query, answer)
        return answer

    context = "\n".join([d.page_content for d in docs])
    prompt = f"""
You are a precise and detailed assistant. Use ONLY the information provided in the context below.
If the answer cannot be found, respond exactly with:
"The answer is not available in the provided documents."

Context:
{context}

Question: {query}
Provide a detailed and well-structured explanation:
    """.strip()

    answer = llm(prompt).strip()

    if not answer or "not available" in answer.lower() or "i don't know" in answer.lower():
        answer = "⚠️ The answer is not available in the provided documents."

    save_chat_history(query, answer)
    return answer
