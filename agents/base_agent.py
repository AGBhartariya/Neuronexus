class BaseAgent:
    def receive(self, message: str):
        raise NotImplementedError("All agents must implement the 'receive' method.")