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

num_instances: int = 0
if char_guess == key_word[0]:
    print(char_guess + " found at index 0")
    num_instances = num_instances + 1

if char_guess == key_word[1]:
    print(char_guess + " found at index 1")
    num_instances = num_instances + 1

if char_guess == key_word[2]:
    print(char_guess + " found at index 2")
    num_instances = num_instances + 1

if char_guess == key_word[3]:
    print(char_guess + " found at index 3")
    num_instances = num_instances + 1

if char_guess == key_word[4]:
    print(char_guess + " found at index 4")
    num_instances = num_instances + 1

if num_instances == 0:
    print("No instances of " + char_guess + " found in " + key_word)

if num_instances == 1:
    print("1 instance of " + char_guess + " found in " + key_word)

if num_instances > 1:
    print(str(num_instances) + " instances of " + char_guess + " found in " + key_word)