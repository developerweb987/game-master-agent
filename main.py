from dotenv import load_dotenv
load_dotenv()  # Load .env as early as possible

from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent
from tools.events import generate_event

def main():
    print("Welcome to Game Master Agent!")
    narrator = NarratorAgent()
    monster = MonsterAgent()
    item = ItemAgent()

    while True:
        choice = input("\nWhat do you want to do? (explore/fight/quit): ").lower()

        if choice == "quit":
            print("Thanks for playing!")
            break

        story = narrator.narrate(choice)
        print("\nStory:\n", story)

        event = generate_event()
        if event == "monster_attack":
            print("\nA monster appears!")
            combat = monster.fight()
            print(combat)
        elif event == "find_item":
            print("\nYou discovered a reward!")
            reward = item.reward()
            print(reward)
        else:
            print("\nYou travel peacefully...")

if __name__ == "__main__":
    main()
