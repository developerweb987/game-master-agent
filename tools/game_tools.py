import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def generate_event():
    events = [
        "You find a hidden cave.",
        "A wild monster appears!",
        "You discover a magical scroll.",
        "A trap is triggered!",
        "A friendly traveler offers help."
    ]
    return random.choice(events)
