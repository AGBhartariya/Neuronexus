# agents/therapy_agent.py

from core.llm_interface import ask_llm

class TherapyAgent:
    def receive(self, message: str):
        system_prompt = (
            "You are a compassionate and supportive mental wellness assistant. "
            "Help users feel better with helpful, calming suggestions."
        )
        return ask_llm(message, system=system_prompt)
