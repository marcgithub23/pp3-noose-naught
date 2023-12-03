import random
from words import animals

print("Welcome to hangman")
print("---------------------------")

# Choose a random word to guess
word_to_guess = random.choice(list(animals)).upper()
# Display and replace letters to guess with a blank
for char in word_to_guess:
    print("_", end=" ")