import random
from words import animals

def get_word():
    """
    Choose word randomly from a dict and uppercase.
    Credit: Kite
    """
    word = random.choice(list(animals))
    return word.upper()

def play(word):
    """Start and play hangman game"""
    # Replace letters with blanks
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    lives = 6

    print("Let's play Hangman!")
    print(f"Lives: {lives}")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")

    while not guessed and lives > 0:
        # Strip any leading and/or trailing whitespace and convert to uppercase
        guess = input("Please guess a letter: ").strip().upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"Oh no, the letter {guess} is not in the word. You've lost one life!")
                # Subtract one life for wrong guess
                lives -= 1
                # Add guessed letter to list for user's reference
                guessed_letters.append(guess)
            else:
                print(f"Good job, the letter {guess} is in the word! You won't lose to the noose yet!")
                guessed_letters.append(guess)
                # Make word_completion to a list
                word_as_list = list(word_completion)
                # Iterate over word to find index where guess is correct
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # Replace blank with correct guess
                for index in indices:
                    word_as_list[index] = guess
                word_completion = " ".join(word_as_list)
                # Game won if all letters in word guessed
                if "_" not in word_completion:
                    guessed = True

        # Validate user input
        else:
            if len(guess) != 1:
                print("Please enter one letter only.")
            elif not guess.isalpha():
                print("Please enter an alphabet only.")
        
        # Print updated game state
        print(f"Lives: {lives}")
        print(display_hangman(lives))
        print(word_completion)
        print(f"You have already entered the following letters: {guessed_letters}")
        print("\n")
    
    # When game is won
    if guessed:
        if lives == 1:
            lives_left = f"{lives} life left"
        else:
            lives_left = f"{lives} lives left"
        print(f"Congratulations, you guessed the word! You escaped the noose with {lives_left}!")
    
    # When game over
    else:
        print(f"Oh no, you're out of lives! You snooze, you're noosed! The word was {word}.")

def display_hangman(lives):
    """
    Display hangman visuals according to lives left.
    Credit: Kite
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]