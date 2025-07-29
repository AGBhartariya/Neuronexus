from agents.base_agent import BaseAgent
from core.memory_store import MemoryStore
from datetime import datetime
# agents/memory_agent.py

from core.memory_store import MemoryStore

class MemoryAgent:
    def __init__(self):
        self.memory_log = []

    def receive(self, message):
        self.memory_log.append({
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        return f"Stored memory: '{message}'"

    def get_recent_memories(self, n=5):
        return self.memory_log[-n:]

