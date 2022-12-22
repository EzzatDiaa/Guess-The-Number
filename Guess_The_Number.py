import random
from art import logo

CHANCES = 0


def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty_level == "hard":
        return CHANCES + 5

    else:
        CHANCES + 10


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print(f"Too high")
        return turns - 1
    elif guess < answer:
        print(f"Too low")
        return turns - 1
    elif guess == answer:
        print(f"You got it right!!, the answer was{answer}")


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
