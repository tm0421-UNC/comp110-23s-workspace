"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730391892"

key_word: str = input("Enter a 5-character word: ")
if len(key_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char_guess: str = input("Enter a single character: ")
if len(char_guess) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + char_guess + " in " + key_word)

for x in range(len(key_word)):
    if key_word[x] == char_guess:
        print(char_guess + " found at index " + str(x))

num_instances: int = sum(char == char_guess for char in key_word)
if num_instances == 1:
    print(str(num_instances) + " instance of " + char_guess + " found in " + key_word)
else: 
    if num_instances > 1:
        print(str(num_instances) + " instances of " + char_guess + " found in " + key_word)
    else:
        print("No instances of " + char_guess + " found in " + key_word)