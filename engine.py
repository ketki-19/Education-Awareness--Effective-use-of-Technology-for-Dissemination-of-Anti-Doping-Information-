import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-placeholder")

ANTIDOPING_KEYWORDS = [
    'doping', 'anti-doping', 'wada', 'nada', 'prohibited', 'substance', 'tue',
    'therapeutic use', 'athlete', 'clean sport', 'testosterone', 'epo', 'sample',
    'dco', 'doping control', 'test', 'ban', 'supplement', 'health', 'ethics',
    'violation', 'adrv', 'sanction', 'medication', 'check'
]

def is_antidoping_query(prompt: str) -> bool:
    prompt_lower = prompt.lower()
    return any(kw in prompt_lower for kw in ANTIDOPING_KEYWORDS)

def generate_ai_response(prompt: str, language: str = 'en') -> str:
    if not is_antidoping_query(prompt):
        if language == 'hi':
            return "मैं केवल डोपिंग रोधी (Anti-Doping), स्वच्छ खेल (Clean Sport), वाडा नियमों, प्रतिबंधित पदार्थों और एथलीट शिक्षा से संबंधित प्रश्नों के उत्तर दे सकता हूँ।"
        return "I can only assist with Anti-Doping, Clean Sport, WADA regulations, prohibited substances, and athlete education."

    system_prompt = (
        "You are an expert Anti-Doping and Clean Sport AI Advisor aligned with WADA 2026 standards. "
        "Provide accurate, strict guidance. Never recommend or give instructions on how to dope. "
        "Emphasize the Strict Liability principle. Always advise consulting official medical professionals and Global DRO."
    )

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception:
        return (
            "As a WADA-aligned educator: Athletes are strictly responsible for any prohibited substance found in their body. "
            "Please verify all medications through official resources like Global DRO and consult your team doctor."
        )