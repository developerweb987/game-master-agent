import random

def generate_event():
    events = ["monster_attack", "find_item", "peaceful_path"]
    return random.choice(events)
