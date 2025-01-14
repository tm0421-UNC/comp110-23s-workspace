"""EX03 - Wordle - Structured Wordle. The full Wordle experience!"""

__author__ = "730391892"

secret_word: str = "codes"


def contains_char (secret_word: str, char_guess: str) -> bool:
    """Checks a string for a single character located at any index of the string."""
    assert len(char_guess) == 1
    idx: int = 0
    char_elsewhere = False
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            char_elsewhere = True
        idx = idx + 1
    return char_elsewhere


def emojified (guess: str, secret_word: str) -> str:
    """Creates an emoji string."""
    assert len(guess) == len(secret_word)
    x: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_str: str = ""
    while x < len(guess):
        if guess[x] == secret_word[x]:
            emoji_str = emoji_str + GREEN_BOX
        else:
            if contains_char(secret_word, guess[x]) is True:
                emoji_str = emoji_str + YELLOW_BOX
            else:
                emoji_str = emoji_str + WHITE_BOX
        x = x + 1
    return emoji_str


def input_guess (exp_len: int) -> str:
    """Prompts the user for a guess with length equal to the secret word."""
    exp_len = len(secret_word)
    guess = input(f"Enter a {exp_len} character word: ")
    while len(guess) != exp_len:
        guess = input(f"That wasn't {exp_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    game_won: bool = False
    guess: str = input_guess(len(secret_word))
    while turn < 7 and game_won is False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            game_won = True
        turn = turn + 1
    if game_won is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print(f"{turn}/6 - Sorry, try again tomorrow!")
    return


main()