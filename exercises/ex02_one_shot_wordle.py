"""EX02 - One shot wordle - Wordle with a single guess."""

__author__ = "730391892"

secret_word: str = "python"
word_len: int = len(secret_word)
guess: str = input(f"What is your {word_len}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
emoji_str: str = ""
char_elsewhere: bool = False
alt_idx: int = 0

#check that the guess is the same length as the secret word
while int(len(guess)) != int(len(secret_word)):
    guess = input(f"That was not {word_len} letters! Try again: ")

#look at each character in the guess
while idx < len(secret_word):
    #check if the guess and the secret word have the same character at the same index
    if guess[idx] == secret_word[idx]:
        #update the emoji string to show correct character and index
        emoji_str = emoji_str + GREEN_BOX
    else: 
        #check if a guessed character occurs elsewhere in the secret word
        while (char_elsewhere == False and alt_idx < len(secret_word)):
            if guess[idx] == secret_word[alt_idx]:
                char_elsewhere = True
            alt_idx = alt_idx + 1
        #update the emoji string based on if the guessed character appears in the secret word
        if char_elsewhere == True:
            emoji_str = emoji_str + YELLOW_BOX
        else: 
            emoji_str = emoji_str + WHITE_BOX
    alt_idx = 0
    char_elsewhere = False
    idx = idx + 1
print(emoji_str)

#check if the guess is the secret word
if guess == secret_word:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")