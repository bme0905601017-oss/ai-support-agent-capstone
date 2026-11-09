import re

def scrub_pii(text: str) -> str:
    """Masks fixed-format phone numbers and checks for prompt injection."""
    injection_patterns = ["ignore previous instructions", "system prompt", "reveal instructions"]
    for pattern in injection_patterns:
        if pattern in text.lower():
            raise ValueError("Guardrail triggered: Potential prompt injection detected.")
            
    # Mask 10-digit phone numbers
    masked_text = re.sub(r'\b\d{10}\b', '[REDACTED_PHONE]', text)
    return masked_text
