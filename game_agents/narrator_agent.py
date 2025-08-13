from agents import Agent

class NarratorAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="NarratorAgent",
            instructions="You narrate the story and describe the adventure for the player."
        )
