# core/agent_bus.py

from agents.memory_agent import MemoryAgent
from agents.therapy_agent import TherapyAgent

class AgentBus:
    def __init__(self):
        self.agents = [MemoryAgent(), TherapyAgent()]  # Add more later!

    def broadcast(self, message: str):
        responses = []
        for agent in self.agents:
            response = agent.receive(message)
            responses.append(response)
        return responses
