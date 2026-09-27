import random

def random_guess():
    while True:
        try:
            print("Welcome to the Random Number Guessing Game!")
            guess = int(input("Guess a number between 1-100: "))
            if guess < 1 or guess >100:
                print("Please enter a number between 1 and 100")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    number = random.randint(1, 100)
    if guess == number:
        print(f"Congratulations! You guessed the correct number: {number}")
    elif guess < number:
        print(f"Too low! The correct number was {number}.")
    else:
        print(f"Too high! The correct number was {number}.")

random_guess()