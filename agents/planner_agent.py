from agents.base_agent import BaseAgent
import google.generativeai as genai

class PlannerAgent(BaseAgent):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def receive(self, message: str):
        prompt = f"Create a step-by-step plan to help with the following task or problem:\n\n{message}"
        response = self.model.generate_content(prompt)
        return response.text.strip()
