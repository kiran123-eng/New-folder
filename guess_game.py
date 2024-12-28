import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the user's guess and give feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
