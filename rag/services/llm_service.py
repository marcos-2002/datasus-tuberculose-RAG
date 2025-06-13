from google import genai
from config import Config

config = Config()

class LLM_service:
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyAqzEgGxmdLpFPuwQ5SOJ2eslqdqvOdsak")

    async def ask_question(self, instructions: str, context: list[str], question: str):
        messages = [
            {"role": "user", "parts": [{"text": instructions}]},
            {"role": "user", "parts": [{"text": f"Pergunta: {question}"}]} 
        ]

        for ctx in context:
            messages[-1]["parts"].append({"text": ctx})

        response = self.client.models.generate_content(
            model="gemini-1.5-pro",
            contents=messages,
        )
        return response.text
    
    async def generate_embedding(self, question):
        return [1, 1, 1, 1]
