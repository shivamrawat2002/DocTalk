## Phase 1

- pymupdf(C under the hood) way faster than pypdf(native python) for parsing
- simple_search is keyword based, not semantic — misses context heavy queries
- chunking at 1000 chars with 200 overlap, need to test if size affects answers
-Optimized PDF ingestion pipeline by replacing pure-Python parser (pypdf) with C-bound MuPDF library (pymupdf), significantly reducing text extraction latency and improving chunk quality for downstream RAG retrieval


Difference with chunking strategies
            semantic	recursive
chunking	59.34s	     0.01s
chunks	      414	     1084
input tokens 13215	      1205
LLM response	7.49s	 1.94s
cost/query	$0.002006	 $0.000210