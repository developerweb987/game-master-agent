from config import get_gemini_model
from tools.dice import roll_dice

class MonsterAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def fight(self):
        player_roll = roll_dice(12)
        monster_roll = roll_dice(12)

        result = "You defeated the monster!" if player_roll >= monster_roll else "You were defeated!"
        prompt = f"A battle occurs. Player rolled {player_roll}, monster rolled {monster_roll}. {result} Describe the fight."

        response = self.model.generate_content(prompt)
        return response.text
