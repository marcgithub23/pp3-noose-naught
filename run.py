import random
import time
import os
from simple_term_menu import TerminalMenu
from words import words_list, definitions
from hangman_visuals import stages


def clear():
    """Clear terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_word(values):
    """Print and display word to guess"""
    print()
    print("\t\t", end=" ")
    for x in values:
        print(x, end=" ")
    print()


def play(word):
    """Start and play hangman game"""
    word_display = []
    definition = definitions[word.lower()]
    guessed = False
    guessed_letters = []
    correct_letters = []
    lives = 6
    hint = 1
    output_message = ""
    quit = False

    for char in word:
        # If alphabet letter, replace with blank space and display
        if char.isalpha():
            word_display.append("_")
        # Otherwise, display if char is space, for example
        else:
            word_display.append(char)

    while not guessed and lives > 0 and not quit:
        clear()
        print(display_hangman(lives))
        print_word(word_display)
        print()
        if hint == 0:
            print(f"Definition of the word: {definition}\n")
        print(f"You tried the following letters: {guessed_letters}\n")
        print(f"Lives: {lives}")
        print(f"Hint available: {hint}\n")
        print(f"{output_message}\n")
        # Strip any leading and/or trailing whitespace and convert to uppercase
        guess = input("Please guess a letter:\n").strip().upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                output_message = f"You already guessed the letter {guess}."
            elif guess not in word:
                output_message = f"{guess} is not in the word. Minus 1 life!"
                # Subtract one life for wrong guess
                lives -= 1
                # Add guessed letter to list for user's reference
                guessed_letters.append(guess)
            else:
                output_message = f"Good job, {guess} is in the word!"
                guessed_letters.append(guess)
                correct_letters.append(guess)
                # Replace blank with correct guess
                for i in range(len(word)):
                    if word[i] == guess:
                        word_display[i] = guess

                # Game won if all letters in word guessed
                if "_" not in word_display:
                    guessed = True

        # Validate user input
        else:
            if len(guess) > 1 and guess != "HINT" and guess != "QUIT":
                output_message = "Please enter one letter only."
            elif len(guess) == 0:
                output_message = "No letter entered. Please enter a letter."
            elif not guess.isalpha():
                output_message = "Please enter an alphabet only."

        # Hint option
        if guess == "HINT":
            # List yes and no options
            options = ["Yes", "No"]
            options_menu = TerminalMenu(options)

            while True:
                print("\nUse hint in exchange for 3 lives?")
                try:
                    options_index = options_menu.show()
                    options_choice = options[options_index]
                    if options_choice == "No":
                        break
                    elif options_choice == "Yes":
                        if lives > 3:
                            output_message = "Exchanged 3 lives for a hint."
                            lives -= 3
                            hint -= 1
                        elif hint == 0:
                            output_message = "You've already used hint."
                        else:
                            output_message = "Not enough lives left."
                        break
                # Catch and handle any errors
                except Exception as e:
                    print(f"An error occured: {e}\n")
                    print("Invalid option!\n")
                    print("Please use the arrow keys to navigate through")
                    print("the available options and hit enter")
                    print("to select your choice.\n")

        # Quit option
        if guess == "QUIT":
            # List yes and no options
            options = ["Yes", "No"]
            options_menu = TerminalMenu(options)

            while True:
                print("\nQuit to game menu?")
                try:
                    options_index = options_menu.show()
                    options_choice = options[options_index]
                    if options_choice == "No":
                        break
                    elif options_choice == "Yes":
                        quit = True
                        break
                # Catch and handle any errors
                except Exception as e:
                    print(f"An error occured: {e}\n")
                    print("Invalid option!\n")
                    print("Please use the arrow keys to navigate through")
                    print("the available options and hit enter")
                    print("to select your choice.\n")

    # When quitting
    if quit:
        print("\nThank you for attempting!\n")
        print("Going back to the game menu...\n")
        print("Please wait a moment...\n")
        # Delay to give illusion of loading and time to read message
        time.sleep(5)
        clear()

    # When game is won
    elif guessed:
        clear()
        display_hangman_win()
        print_word(word_display)

        if lives == 1:
            lives_left = f"{lives} life left"
        else:
            lives_left = f"{lives} lives left"

        print(f"\nCongratulations, you guessed the word {word}!")
        print(f"You escaped the noose with {lives_left}!\n")
        print("Going back to the game menu...\n")
        print("Please wait a moment...\n")
        # Delay to give user time to read final result and back to game menu
        # Credit: Fabio Musanni
        time.sleep(10)

    # When game over
    else:
        clear()
        print(display_hangman(lives))
        print_word(word_display)
        if len(correct_letters) == 1:
            num_correct_letters = f"{len(correct_letters)} letter"
        else:
            num_correct_letters = f"{len(correct_letters)} letters"
        print("\nToo bad, you're out of lives!")
        print("You snooze, you're noosed!")
        print(f"You guessed {num_correct_letters} correctly.")
        print(f"But the word was {word}.\n")
        print("Going back to the game menu...\n")
        print("Please wait a moment...\n")
        # Delay to give user time to read final result and back to game menu
        time.sleep(10)


def display_hangman(lives):
    """Display hangman visuals according to lives left."""
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


def print_game_menu():
    """Display game menu"""

    print(f"""

        -----------------------------------------------------------------------
        |                               GAME MENU                             |
        -----------------------------------------------------------------------

        Welcome to Noose Naught, a hangman game.

        Game Instructions:
        - You have 6 lives (or tries) to guess the word.
        - You can use 1 hint in exchange for 3 lives by typing "hint".
        - You need at least 4 lives to use 1 hint and continue the game.
        - You only have 1 hint available.
        - The hint is the definition of the word.
        - To quit a game in progress, type "quit" to go back to the game menu.

        Ready to play and put your neck in the noose?

        Using the arrow keys, please select a word category below and hit enter
        or select quit and hit enter to exit program.

        """)


def game_menu_options():
    """
    Display game menu with simple term menu
    Credit: Chad Thackray
    """

    # List available options
    options = ["Animals", "Verbs", "Uncommon words", "Quit"]
    main_menu = TerminalMenu(options)
    quit = False

    while not quit:
        clear()
        print_game_menu()
        try:
            options_index = main_menu.show()
            options_choice = options[options_index]

            # Exit program
            if options_choice == "Quit":
                print("Thank you for playing!\n")
                print("Closing the program...\n")
                print("Please wait a moment...\n")
                quit = True
                # Delay to give illusion of exiting and time to read message
                time.sleep(5)
                clear()
            # Get random word from category of choice and start game
            else:
                clear()
                # Change to lower case to match keys
                options_choice = options_choice.lower()
                word = random.choice(words_list[options_choice]).upper()
                play(word)
        # Catch and handle any errors
        except Exception as e:
            print(f"An error occured: {e}\n")
            print("Invalid option!\n")
            print("Please use the arrow keys to navigate through")
            print("the available options and hit enter")
            print("to select your choice.\n")
            print("Reloading... Please wait a moment...")
            # Delay to give user time to read error message before cleared
            time.sleep(7)


def main():
    """Run all program functions"""
    game_menu_options()


if __name__ == "__main__":
    main()
