import time
import streamlit as st

def simple_search(query: str, chunks: list[str], top_k: int = 5) -> list[str]:
    query_words = set(query.lower().split())
    scored = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(query_words & chunk_words)
        scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [chunk for _, chunk in scored[:top_k]]

def log_time(label: str, start: float):
    elapsed = time.time() - start
    st.sidebar.write(f"⏱ {label}: `{elapsed:.2f}s`")
    return elapsed