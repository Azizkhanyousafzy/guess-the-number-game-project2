import random

def guess_the_number():
    """Project 2: Guess the Number Game By Computer."""
    number = random.randint(1, 100)
    guesses_left = 7
    # welcome message
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    # Loop for guesses
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input: please enter a number.")
            continue

        # Check the guess
        if guess < number:
            print("Too low! Try another number.")
        elif guess > number:
            print("Too high! Try another number.")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries!")
            return

        guesses_left -= 1

    # When all guesses are used
    print(f"\nYou ran out of guesses! The number was {number}.")

guess_the_number()