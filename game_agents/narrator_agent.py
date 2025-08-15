from agents import Agent
from tools.game_tools import generate_event

narrator_agent = Agent(
    name="NarratorAgent",
    instructions="Keep the story short. Call generate_event() when user explores.",
    model=None,
    handoffs=[]
)
