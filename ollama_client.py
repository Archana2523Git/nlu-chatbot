import requests
import json

class OllamaClient:
    def __init__(self, model="llama3.2:1b", server_url="http://127.0.0.1:11434"):
        self.model = model
        self.server_url = server_url.rstrip("/")
        self.api_endpoint = f"{self.server_url}/api/generate"

        # Intent-locked behavior (MENTOR SAFE)
        self.intent_behavior = {
            "greeting": "Greet the user politely in one short sentence.",
            "book_flight": "Ask for departure city, destination, and travel date only.",
            "check_time": "Ask which city they want the current time for.",
            "goodbye": "Say goodbye briefly.",
            "fallback": "Ask the user to rephrase their request clearly."
        }

    def generate(self, user_input, predicted_intent, stream=False):
        behavior = self.intent_behavior.get(
            predicted_intent,
            "Respond briefly and stay on task."
        )

        prompt = f"""
You are a controlled NLU assistant.
Your job is to respond ONLY according to the given intent.

Intent: {predicted_intent}
Behavior rule: {behavior}

User input: {user_input}

Response:
""".strip()

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "options": {
                "temperature": 0.2,
                "num_predict": 50
            }
        }

        try:
            response = requests.post(
                self.api_endpoint,
                json=payload,
                timeout=15
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()

        except requests.exceptions.Timeout:
            return "LLM timeout. Please try again."

        except requests.RequestException as e:
            return f"Ollama error: {e}"

        except json.JSONDecodeError:
            return "Invalid response from Ollama."
