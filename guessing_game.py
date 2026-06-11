# Guessing Game (1-100)
import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the guessing game!")
print("I'm thinking a number between 1 and 100")

while True:
    guess = int(input("Enter your guessed number: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You have guessed the number in {attempts} attempts")
        print(f"The number was {secret_number}")
        break
