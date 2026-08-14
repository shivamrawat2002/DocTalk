from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

GPT4O_MINI_INPUT = 0.150 / 1_000_000   # per token
GPT4O_MINI_OUTPUT = 0.600 / 1_000_000  # per token

def get_answer(query: str, chunks: list[str], api_key: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

    context = "\n\n".join(chunks[:5])

    prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer using only the context below.
If the answer is not in the context, say "I couldn't find that in the document."

Context: {context}

Question: {question}
""")

    chain = prompt | llm
    response = chain.invoke({"context": context, "question": query})

    input_tokens = response.usage_metadata["input_tokens"]
    output_tokens = response.usage_metadata["output_tokens"]
    cost = (input_tokens * GPT4O_MINI_INPUT) + (output_tokens * GPT4O_MINI_OUTPUT)

    return {
        "answer": response.content,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost": cost
    }