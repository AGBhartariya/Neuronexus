from agents.emotion_agent import EmotionAgent
from agents.imagination_agent import ImaginationAgent
from agents.planner_agent import PlannerAgent
from agents.therapy_agent import TherapyAgent
from agents.memory_agent import MemoryAgent

class ConductorAgent:
    def __init__(self):
        self.agents = {
            "Memory": MemoryAgent(),
            "Emotion": EmotionAgent(),
            "Imagination": ImaginationAgent(),
            "Planner": PlannerAgent(),
            "Therapy": TherapyAgent()
        }

    def receive(self, message: str) -> dict:
        responses = {}
        for name, agent in self.agents.items():
            responses[name] = agent.receive(message)
        return responses
