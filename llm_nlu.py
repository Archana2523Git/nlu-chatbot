import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are a high-accuracy NLU engine.

Your job is to extract:
- intent
- entities

Return ONLY valid JSON in this format:

{
  "intent": "",
  "confidence": 0.0,
  "entities": {},
  "reason": ""
}
"""

def analyze(text):
    payload = {
        "model": "llama3.2:1b",
        "prompt": SYSTEM_PROMPT + "\nUser: " + text + "\nReturn JSON only.",
        "format": "json",
        "options": {
            "temperature": 0.1,
            "num_ctx": 1024,
            "num_predict": 256
        },
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=120)
        data = r.json()
    except Exception as e:
        return {
            "intent": "fallback",
            "confidence": 0.0,
            "entities": {},
            "reason": f"Ollama connection error: {str(e)}"
        }

    if "response" in data:
        raw = data["response"]
    elif "message" in data and "content" in data["message"]:
        raw = data["message"]["content"]
    else:
        return {
            "intent": "fallback",
            "confidence": 0.0,
            "entities": {},
            "reason": f"Unexpected Ollama output: {data}"
        }

    try:
        return json.loads(raw)
    except:
        return {
            "intent": "fallback",
            "confidence": 0.0,
            "entities": {},
            "reason": "LLM did not return valid JSON",
            "raw_output": raw
        }
