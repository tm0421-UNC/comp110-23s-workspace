"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730391892"

chardle_word: str = input("Enter a 5-character word: ")
if len(chardle_word)!=5:
    print("Error: Word must contain 5 characters")
    exit()
char_guess: str = input("Enter a single character: ")
if len(char_guess)!=1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + char_guess + " in " + chardle_word)

for i in range(len(chardle_word)):
    if(chardle_word[i] == char_guess):
      print(char_guess+" found at index "+ str(i))

numb_instances: int=sum(char==char_guess for char in chardle_word)
if numb_instances!=0:
    print(str(numb_instances)+" instances of "+char_guess+" found in "+chardle_word)
else:
    print("No instances of "+char_guess+" found in "+chardle_word)