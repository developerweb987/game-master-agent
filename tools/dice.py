import random

def roll_dice(sides=6):
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)
