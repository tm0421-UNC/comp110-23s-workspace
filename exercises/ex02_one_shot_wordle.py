"""EX02 - One shot wordle - Wordle with a single guess."""

__author__ = "730391892"

secret_word: str = "python"
word_len: int = len(secret_word)
guess: str = input(f"What is your {word_len}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
index_emoji: str = ""
char_elsewhere: bool = False
alt_idx: int = 0

while int(len(guess)) != int(len(secret_word)):
    guess = input(f"That was not {word_len} letters! Try again: ")

while idx < len(secret_word):
    if guess[idx] == secret_word[idx]:
        index_emoji = index_emoji + GREEN_BOX
    else: 
        while (char_elsewhere == False and alt_idx < len(secret_word)):
            if guess[idx] == secret_word[alt_idx]:
                char_elsewhere = True
            alt_idx = alt_idx + 1
        if char_elsewhere == True:
            index_emoji = index_emoji + YELLOW_BOX
        else: 
            index_emoji = index_emoji + WHITE_BOX
    alt_idx = 0
    char_elsewhere = False
    idx = idx + 1
print(index_emoji)

if guess == secret_word:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")