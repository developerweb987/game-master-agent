import random

def roll_dice(sides: int = 20) -> int:
    return random.randint(1, sides)

def generate_event() -> str:
    events = [
        "You find a mossy clearing with strange runes.",
        "A dark cave mouth yawns ahead.",
        "A little bridge crosses a rushing stream.",
        "You meet a cloaked traveler who offers a hint.",
        "Footprints of a beast lead into the trees."
    ]
    return random.choice(events)

def damage_roll() -> int:
    return random.randint(1, 8)

def monster_hp() -> int:
    return random.randint(8, 14)
