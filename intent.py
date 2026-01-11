import re

GREETINGS = [
    "hi", "hello", "hey", "good morning", "good evening"
]

HIGH_INTENT_KEYWORDS = [
    "signup", "buy", "purchase", "subscribe",
    "get started", "start subscription", "pro plan looks good",
    "i want to buy", "i want to purchase"    
]

INQUIRY_KEYWORDS = [
    "price", "pricing", "cost", "plans", "features",
    "refund", "policy", "support", "resolution", "know", "about","pro plan", "basic plan", "policies"
]

def classify_intent(message: str) -> str:
    """
    Classifies user intent into:
    - greeting
    - inquiry
    - high_intent
    """
    text = message.lower().strip()

    # Greeting check
    if any(greet in text for greet in GREETINGS):
        return "greeting"

    # High intent check (priority)
    if any(keyword in text for keyword in HIGH_INTENT_KEYWORDS):
        return "high_intent"

    # Inquiry check
    if any(keyword in text for keyword in INQUIRY_KEYWORDS):
        return "inquiry"

    # Default fallback
    return "inquiry"
