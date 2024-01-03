import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    low = 1
    high = 100
    secret_number = random.randint(low, high)
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input(f"Guess the number between {low} and {high}: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
number_guessing_game()
