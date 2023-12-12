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
