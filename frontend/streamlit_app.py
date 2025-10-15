import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"  

st.set_page_config(page_title="RAG QA System", layout="wide")
st.title("📘 Domain-Specific Question Answering System")
st.write("Ask questions based only on your uploaded documents.")

if "messages" not in st.session_state:
    st.session_state.messages = []


if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


    try:
        response = requests.post(API_URL, json={"question": prompt}, timeout=30)
        if response.status_code == 200:
            answer = response.json().get(
                "answer",
                "The answer is not available in the provided documents. Please try asking a different question."
            )
            if not answer.strip():
                answer = "The answer is not available in the provided documents. Please try asking a different question."
        else:
            answer = "The answer is not available in the provided documents. Please try asking a different question."
    except requests.exceptions.RequestException:
        answer = "The answer is not available in the provided documents. Please try asking a different question."

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

