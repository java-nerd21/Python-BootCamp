# Easy and hard modes
# Easy has 10 lives
# Hard has 5 lives
#
# Computer picks random number from 1 to 100
#
# player makes a guess
# Computer says if its high or lower and 1 life is remove
# Above is repeated until lives are gone or number is guessed correctly
#
# print message depending on win or lose
#
# Ask do they want to play again

from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Check answer against guess and returns number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100")
    number_to_guess = randint(1, 100)

    turns = set_difficulty()
    guess = 0

    while guess != number_to_guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number_to_guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number_to_guess:
            print("Guess again.")


while input("Do you want to play a Number Guessing Game? Type 'y' or 'n' ") == "y":
    play_game()
