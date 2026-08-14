import pymupdf
def load_pdf(file) -> str:
    doc = pymupdf.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() or ""
    return text

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks