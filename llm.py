# llm.py

def generate_answer(context: str, question: str) -> str:
    """
    Local deterministic response generator.
    Simulates LLM behavior using retrieved context.
    This avoids external API instability for demo purposes.
    """
    return f"Here’s what I found based on our information:\n{context}"
