
import random

secret_number = random.randint(1, 100)
guess = 0

print("Welcome to the Number Guessing Game!")
print("I have generated a number between 1 and 100.")
print("Can you guess what it is?")

while guess != secret_number:

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    # Use if/elif/else statements to provide hints.
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        # If the guess is correct, the loop will terminate, and this message will be shown.
        print(f"Congratulations! You guessed the number {secret_number} correctly!")

