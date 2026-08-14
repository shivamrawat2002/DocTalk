import streamlit as st
from dotenv import load_dotenv
import os

from ingestion.pdf_loader import load_pdf, chunk_text
from llm.query_engine import get_answer
from utils.helpers import simple_search

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="DocTalk", page_icon="📄")
st.title("📄 DocTalk")
st.caption("Chat with your PDF documents")

if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
    if uploaded_file:
        with st.spinner("Parsing & chunking..."):
            text = load_pdf(uploaded_file)
            st.session_state.chunks = chunk_text(text)
        st.success(f"Done! {len(st.session_state.chunks)} chunks created")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if query := st.chat_input("Ask something about your PDF..."):
    if not st.session_state.chunks:
        st.warning("Upload a PDF first")
    else:
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)

        with st.spinner("Thinking..."):
            relevant = simple_search(query, st.session_state.chunks)
            answer = get_answer(query, relevant, api_key)

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)