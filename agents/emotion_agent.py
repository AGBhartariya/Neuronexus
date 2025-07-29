from agents.base_agent import BaseAgent
import google.generativeai as genai

class EmotionAgent(BaseAgent):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def receive(self, message: str):
        prompt = f"Detect the emotion in the following message and reply empathetically:\n\n{message}"
        response = self.model.generate_content(prompt)
        return response.text.strip()
