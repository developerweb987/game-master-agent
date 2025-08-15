from agents import Agent
from tools.game_tools import roll_dice, damage_roll, monster_hp

monster_agent = Agent(
    name="MonsterAgent",
    instructions="Handle combat. Use roll_dice() for hits and damage_roll() for damage.",
    model=None,
    handoffs=[]
)
