import pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(file) -> str:
    doc = pymupdf.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() or ""
    return text


def chunk_text(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_text(text)