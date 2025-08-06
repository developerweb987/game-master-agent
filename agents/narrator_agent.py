from config import get_gemini_model

class NarratorAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def narrate(self, player_choice):
        prompt = f"You are the narrator of a fantasy text game. The player chooses: {player_choice}. Continue the story accordingly."
        response = self.model.generate_content(prompt)
        return response.text
