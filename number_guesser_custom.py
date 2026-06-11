# Number Guesser with Custom Range
import random

def number_guesser():
    print("Welcome to the guessing game!")
    print("\nLet's set the range")
    
    min_val = int(input("Enter the minimum number: "))
    max_val = int(input("Enter the maximum number: "))
    
    secret_number = random.randint(min_val, max_val)
    attempts = 0
    
    print(f"I'm thinking of a number between {min_val} and {max_val}")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low. Try again\n")
        elif guess > secret_number:
            print("Too high. Try again\n")
        else:
            print(f"Congratulations! You have guessed the number in {attempts} attempts")
            print(f"The number was {secret_number}")
            break

number_guesser()
