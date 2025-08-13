import random

def generate_event():
    """Generate a random game event."""
    events = [
        "You find a hidden treasure chest!",
        "A wild monster appears!",
        "You fall into a trap!",
        "You meet a friendly NPC.",
        "You discover a secret passage."
    ]
    return random.choice(events)
