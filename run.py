import random
from words import animals

def get_word():
    """
    Choose word randomly from a dict and uppercase.
    Credit: Kite
    """
    word = random.choice(list(animals))
    return word.upper()