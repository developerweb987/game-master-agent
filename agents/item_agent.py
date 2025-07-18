# agents/item_agent.py

class ItemAgent:
    def give_item(self):
        items = [
            "Sword of Flames 🔥",
            "Shield of Light 🛡️",
            "Potion of Healing 🍷",
            "Ring of Invisibility 💍",
            "Scroll of Teleportation 📜"
        ]
        return f"You found an item: {items[0]}"
