from agents import Agent
from tools.events import generate_event

class ItemAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="ItemAgent",
            instructions="You provide items, rewards, or inventory management in the game."
        )