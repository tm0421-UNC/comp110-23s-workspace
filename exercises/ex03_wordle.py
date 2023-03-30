"""EX03 - Wordle - Structured Wordle. The full Wordle experience!"""

__author__ = "730391892"


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks a string for a single character located at any index of the string."""
    assert len(char_guess) == 1
    idx: int = 0
    char_elsewhere = False
    # Goes through each index of the secret word to check for the guessed character.
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            char_elsewhere = True
        idx = idx + 1
    return char_elsewhere


def emojified(guess: str, secret_word: str) -> str:
    """Creates an emoji string."""
    assert len(guess) == len(secret_word)
    idx: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_str: str = ""
    # Checks each index of the secret word.
    while idx < len(guess):
        # Returns an emoji if the characters are equal at a certain index 
        if guess[idx] == secret_word[idx]:
            emoji_str = emoji_str + GREEN_BOX
        else:
            # Uses the contains_char function to check if a character appears in the word and assigns the appropriate emoji.
            if contains_char(secret_word, guess[idx]) is True:
                emoji_str = emoji_str + YELLOW_BOX
            else:
                emoji_str = emoji_str + WHITE_BOX
        idx = idx + 1
    return emoji_str


def input_guess(exp_len: int) -> str:
    """Prompts the user for a guess with length equal to the secret word."""
    guess = input(f"Enter a {exp_len} character word ")
    # Checks that the user's guess is the same length as the secret word.
    while len(guess) != exp_len:
        guess = input(f"That wasn't {exp_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "76f8fftiftfit"
    x: int = 0
    game_won: bool = False
    turn: int = 0
    # Prompts user for a guess while they still have turns left and the game is not won.
    while x < 6 and game_won is False:
        turn = turn + 1
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            game_won = True
        x = x + 1
    # Prints message indicating to the user the outcome of the game and the number of turns.
    if game_won is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print(f"{turn}/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()