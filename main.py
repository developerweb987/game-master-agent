# main.py

from agents import NarratorAgent, MonsterAgent, ItemAgent
from tools import roll_dice, generate_event

def main():
    print("🎮 Welcome to the Game Master Agent - Fantasy Adventure Game")
    player_name = input("Enter your adventurer's name: ")

    narrator = NarratorAgent()
    monster = MonsterAgent()
    item = ItemAgent()

    while True:
        print("\n🌟 New Scene:")
        scene = narrator.narrate_scene(player_name)
        print(scene)

        if "monster" in scene.lower():
            print("\n⚔️ Combat Phase:")
            result = monster.combat(player_name)
            print(result)
        elif "item" in scene.lower() or "scroll" in scene.lower():
            print("\n🎁 Loot Phase:")
            reward = item.give_item()
            print(reward)

        cont = input("\nDo you want to continue your adventure? (yes/no): ").lower()
        if cont != "yes":
            print("🧝‍♂️ Farewell, brave adventurer!")
            break

if __name__ == "__main__":
    main()
