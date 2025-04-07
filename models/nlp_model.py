from transformers import pipeline

# Force PyTorch backend (default)
intent_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", framework="pt")

def detect_intent(message: str):
    labels = ["follow-up", "new symptoms", "emergency"]
    result = intent_pipeline(message, labels)
    return result["labels"][0]

def extract_symptoms(message: str):
    # Very basic example - replace with proper NER if needed
    keywords = ["fever", "cough", "headache", "nausea", "cold", "pain", "dizziness"]
    return [word for word in keywords if word in message.lower()]
