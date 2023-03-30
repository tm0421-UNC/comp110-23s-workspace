"""EX06 - Create your own adventure - Number guessing game. Roulette with much less options."""

__author__ = "730391892"

points: int = 0
player: str = ""
game_end: bool = False
ROCKET_EMOJI: str = "\U0001F680"
STAR_EMOJI: str = "\u2B50"
CLOVER_EMOJI: str = "\u2618"
CARD_EMOJI: str = "\U0001F0A1"
NERVOUS_EMOJI: str = "\U0001F62C"
SAD_EMOJI: str = "\U0001F622"
WAVE_EMOJI: str = "\U0001F44B"


def greet() -> None:
    """Greets the user and requests input to initialize the player name."""
    global player
    print(f"Welcome to the number guessing game, a very simplified version of roulette.{CARD_EMOJI}\nEach turn a die will be rolled, and you may either guess the number or whether the rolled\nnumber will be even.\nYou will receive 3 points for guessing the correct number, 1 point for correctly guessing\nwhether the number will be even, or 0 points if you are incorrect.\nAn incorrect guess will end the game. Good luck!")
    player = input("What is your name? ")


def turn_exact() -> None:
    """Simulates a random die roll and prompts the user for an exact numerical guess."""
    from random import randint
    global game_end, player, points
    guess = input(f"Feeling lucky {player}?{CLOVER_EMOJI} Type a number 1 - 6: ")
    roll: int = randint(1, 6)
    while int(guess) > 6 and int(guess) < 1:
        guess = input(f"{player} you must choose a number between 1 - 6: ")
    print(f"Guess: {guess} , Rolled number: {roll}")
    if int(guess) == roll:
        points += 3
        print(f"Wow {player}! Great guess! You now have {points} points! {ROCKET_EMOJI}")
    else:
        print(f"Sorry {player}, your guess was incorrect!{SAD_EMOJI} You ended with {points} total points!")
        game_end = True


def turn(score: int) -> int:
    """Simulates a random die roll and asks the user whether the roll will be even or odd."""
    from random import randint
    global game_end, player
    point_total: int = score
    guess = input(f"Not so confident {player}?{NERVOUS_EMOJI} Type '1' for odd or '2' for even: ")
    while guess != '1' and guess != '2':
        guess = input(f"{player} you must type either 1 or 2 for your guess: ")
    roll: int = randint(1, 6)
    if int(guess) == 1 and roll % 2 == 1: 
        point_total += 1
        print(f"Good guess {player}! {STAR_EMOJI}")
    if int(guess) == 2 and roll % 2 == 0:
        point_total += 1
        print(f"Good guess {player}! {STAR_EMOJI}")
    else:
        print(f"Wrong guess {player}!{SAD_EMOJI}")
        game_end = True
    return point_total


def main() -> None:
    """The main game loop: greets the player and keeps track of points as long as the player hasn't given an incorrect guess or ended the game."""
    global game_end, player
    points = 0
    greet()
    while game_end is False:
        print(f"Total points: {points}")
        choice = input("Press one of the following keys:\n 1 - Guess an exact number\n 2 - Guess even or odd\n 3 - End the game\n")
        if choice == "1":
            turn_exact()
        if choice == "2":
            points = turn(points)
        if choice == "3":
            print(f"Goodbye {player}, thanks for playing!{WAVE_EMOJI} You finished with {points} total points!")
            game_end = True


if __name__ == "__main__":
    main()