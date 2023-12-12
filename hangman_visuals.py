from colorama import Fore


# Credit: Kite
stages = [  # final state: head, torso, both arms, and both legs
            f"""{Fore.RED}
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
            # head, torso, both arms, and one leg
            f"""{Fore.RED}
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
            """,
            # head, torso, and both arms
            f"""{Fore.RED}
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
            """,
            # head, torso, and one arm
            f"""{Fore.RED}
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
            """,
            # head and torso
            f"""{Fore.RED}
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
            """,
            # head
            f"""{Fore.RED}
                --------
                |      |
                |      O
                |
                |
                |
                -
            """,
            # initial empty state
            f"""{Fore.RED}
                --------
                |      |
                |
                |
                |
                |
                -
            """
    ]


hangman_win = f"""{Fore.GREEN}
        --------
        |
        |
        |            O
        |           \\|/
        |            |
        -           / \\
        """


game_menu_text = f"""{Fore.GREEN}

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

"""
