from agents import Agent
from tools.game_tools import generate_event

item_agent = Agent(
    name="ItemAgent",
    instructions="Give rewards or items after events or combat.",
    model=None,
    handoffs=[]
)
