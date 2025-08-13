from agents import Agent
from tools.dice import roll_dice

class MonsterAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="MonsterAgent",
            instructions="You handle battles with monsters when triggered in the game."
        )