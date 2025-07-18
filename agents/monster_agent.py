# agents/monster_agent.py

from tools.game_tools import roll_dice

class MonsterAgent:
    def combat(self, player_name):
        player_roll = roll_dice()
        monster_roll = roll_dice()
        if player_roll >= monster_roll:
            return f"{player_name} defeats the monster! 🎉"
        else:
            return f"{player_name} was defeated by the monster... ☠️"
