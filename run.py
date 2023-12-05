import random
from words import word_categories, words_list, definitions

def print_word(values):
    """Print and display word to guess"""
    print()
    print("\t", end=" ")
    for x in values:
        print(x, end=" ")
    print()

def play(word):
    """Start and play hangman game"""
    word_display = []
    definition = definitions[word.lower()]
    guessed = False
    guessed_letters = []
    lives = 6
    hint = 1
    quit = False

    for char in word:
        # If alphabet letter, replace with blank space and display
        if char.isalpha():
            word_display.append("_")
        # Otherwise, display if char is space, for example
        else:
            word_display.append(char)

    while not guessed and lives > 0 and not quit:
        print(f"Lives: {lives}")
        print(f"Hint available: {hint}")
        print(display_hangman(lives))
        print_word(word_display)
        print()
        if hint == 0:
            print(f"Definition of the word: {definition}")
        print()
        print(f"You have already entered the following letters: {guessed_letters}")
        print()

        # Strip any leading and/or trailing whitespace and convert to uppercase
        guess = input("Please guess a letter: \n").strip().upper()

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
                # Replace blank with correct guess
                for i in range(len(word)):
                    if word[i] == guess:
                        word_display[i] = guess

                # Game won if all letters in word guessed
                if "_" not in word_display:
                    guessed = True

        # Validate user input
        else:
            if len(guess) != 1 and guess != "HINT" and guess != "QUIT":
                print("Please enter one letter only.")
            elif not guess.isalpha():
                print("Please enter an alphabet only.")
        
        # Hint option
        if guess == "HINT":
            hint_answer = input("Are you sure you want to use hint in exchange for 3 lives? (Y/N): \n").upper()
            if hint_answer == "N":
                continue
            else:
                if lives > 3:
                    print(f"You've exchanged 3 lives for a hint.")
                    lives -= 3
                    hint -= 1
                elif hint == 0:
                    print("You've already used hint.")
                else:
                    print("You need at least 4 lives to use hint and continue the game.")

        # Quit option
        if guess == "QUIT":
            quit_answer = input("Are you sure you want to quit and go back to the game menu? (Y/N): \n").upper()
            if quit_answer == "N":
                continue
            else:
                quit = True
    
    # When quitting
    if quit:
        print("Thank you for attempting!")
    
    # When game is won
    elif guessed:
        display_hangman_win()
        print_word(word_display)
        print()
        if lives == 1:
            lives_left = f"{lives} life left"
        else:
            lives_left = f"{lives} lives left"
        print(f"Congratulations, you guessed the word {word}! You escaped the noose with {lives_left}!")
    
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

def display_hangman_win():
    """
    Print out a visual of the man escaping the gallows
    Credit: Scottish Coder
    """
    print(
        """
        --------
        |      
        |      
        |            O
        |           \\|/
        |            |
        -           / \\
        """
    )

def main():
    """Run all program functions"""
    # Game menu to ask user to select a category; Credit: Scottish Coder
    while True:
        print()
        print("---------------------")
        print("\t\tGAME MENU")
        print("---------------------")
        # Display available categories to choose from and exit option
        for key in word_categories:
            print(f"Press {key} to select {word_categories[key]}")
            print(f"Press {len(word_categories) + 1} to exit game")
            print()
        try:
            # Ask user to enter choice and convert to int
            choice = int(input("Enter your choice = \n"))
        except ValueError:
            # Handle error if user enters an invalid choice
            print("Invalid choice! Please select from the available options.")
            continue
        
        # If user enters a number greater than the available options
        if choice > len(word_categories) + 1:
            print("Invalid choice! Please select from the available options.")
            continue
        # If user wants to exit game
        elif choice == len(word_categories) + 1:
            print()
            print("Thank you for playing!")
            break

        chosen_category = word_categories[choice]
        word = random.choice(words_list[chosen_category]).upper()
        play(word)

if __name__ == "__main__":
    main()