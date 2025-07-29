from agents.base_agent import BaseAgent
import google.generativeai as genai

class ImaginationAgent(BaseAgent):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")

    def receive(self, message: str):
        prompt = f"Imagine a creative and helpful response or story based on this input:\n\n{message}"
        response = self.model.generate_content(prompt)
        return response.text.strip()
