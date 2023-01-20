"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730391892"

keyword: str = input("Enter a 5-character word: ")
if len(keyword) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char_guess: str = input("Enter a single character: ")
if len(char_guess) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + char_guess + " in " + keyword)

for i in range(len(keyword)):
    if keyword[i] == char_guess:
        print(char_guess + " found at index " + str(i))

num_instances: int = sum(char == char_guess for char in keyword)
if num_instances == 1:
    print(str(num_instances) + " instance of " + char_guess + " found in " + keyword)
elif num_instances > 1:
    print(str(num_instances) + " instances of " + char_guess + " found in " + keyword)
else:
    print("No instances of " + char_guess + " found in " + keyword)