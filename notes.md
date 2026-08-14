## Phase 1

- pymupdf(C under the hood) way faster than pypdf(native python) for parsing
- simple_search is keyword based, not semantic — misses context heavy queries
- chunking at 1000 chars with 200 overlap, need to test if size affects answers
-Optimized PDF ingestion pipeline by replacing pure-Python parser (pypdf) with C-bound MuPDF library (pymupdf), significantly reducing text extraction latency and improving chunk quality for downstream RAG retrieval