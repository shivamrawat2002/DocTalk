from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def get_answer(query: str, chunks: list[str], api_key: str) -> str:
    llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
    
    context = "\n\n".join(chunks[:5])

    prompt = ChatPromptTemplate.from_template("""
<job>
You are an Legal AI assistant whose task is to help the user answer questions from the context provided.
You can are not just a ruleb-based system but a smart system which understand user intent and provide the relevant answers.
</job>

Context: {context}

Question: {question}

Example:
I am being accused of false crime how can I defend myself?
Article 20(3): Protects you from self-incrimination; you cannot be forced to be a witness against yourself and have the absolute right to remain silent.Article 21: Guarantees your right to life and personal liberty, ensuring that you cannot be deprived of freedom except through a fair, just procedure established by law.Article 22: Gives you the right to be informed of the specific grounds of your arrest, consult a legal practitioner of your choice, and be produced before a magistrate within 24 hours.Article 14: Ensures equality before the law and guards against arbitrary, discriminatory state or police action.
""")

    chain = prompt | llm
    response = chain.invoke({"context": context, "question": query})
    return response.content