import random
import time
from simple_term_menu import TerminalMenu
from words import words_list, definitions

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
        
        if lives == 1:
            lives_left = f"{lives} life left"
        else:
            lives_left = f"{lives} lives left"
        
        print(f"""
            
            Congratulations, you guessed the word {word}!
            You escaped the noose with {lives_left}!
            
            Going back to the game menu...
            
            Please wait a moment...
            
            """)
        
        # Delay to give user time to read final result and back to game menu
        # Credit: Fabio Musanni
        time.sleep(10)
    
    # When game over
    else:
        print(display_hangman(lives))
        print_word(word_display)
        
        print(f"""
            Too bad, you're out of lives!
            You snooze, you're noosed!
            You guessed {len(correct_letters)} letters correctly.
            But the word was {word}.

            Going back to the game menu...
            
            Please wait a moment...
            """)
        
        # Delay to give user time to read final result and back to game menu
        time.sleep(10)

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


def print_game_menu():
    """Display game menu"""
    
    print(f"""
        
        ------------------------------------------------------------------
        |                             GAME MENU                          |
        ------------------------------------------------------------------
        
        Welcome to Noose Naught, a hangman game.
        
        Game Instructions:
        - You have 6 lives (or tries) to guess the word.
        - You can use 1 hint in exchange for 3 lives by typing "hint".
        - You need at least 4 lives to use 1 hint and continue the game.
        - You only have 1 hint available.
        - The hint is the definition of the word.
        - To quit a game in progress, type "quit" to go back to the game menu.
        
        Ready to play and put your neck in the noose?
        
        Using the arrow keys, please select a word category below and hit enter.
        Or select quit and hit enter to exit program.
        
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
        print_game_menu()
        try:
            options_index = main_menu.show()
            options_choice = options[options_index]
            
            # Exit program
            if options_choice == "Quit":
                print("Thank you for playing!")
                quit = True
            # Get random word from category of choice and start game
            else:
                word = random.choice(words_list[options_choice.lower()]).upper()
                play(word)
        # Catch and handle any errors
        except Exception as e:
            print(f"""
                
                An error occured: {e}
                
                Invalid option!
                
                Please use the arrow keys to navigate through the available
                options and hit enter to select your choice.

                """)


def main():
    """Run all program functions"""
    game_menu_options()

if __name__ == "__main__":
    main()