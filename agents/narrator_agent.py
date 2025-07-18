# agents/narrator_agent.py

from tools.game_tools import generate_event

class NarratorAgent:
    def narrate_scene(self, player_name):
        event = generate_event()
        return f"{player_name}, {event}"
