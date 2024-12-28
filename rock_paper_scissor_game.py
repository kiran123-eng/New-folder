import random

# Select the computer's choice
com = random.choice(["rock", "paper", "scissors"])

print("Welcome to the game show!")
print("You vs Computer")

# Initialize attempt counter and player's turn
attempt = 0
your_turn = None

while your_turn != com:
    # Take user's input
    your_turn = input("Enter your choice: rock, paper, or scissors: ").lower()

    # Handle invalid input
    if your_turn not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue  # Skip the rest of the loop and prompt again

    attempt += 1  # Increment attempt counter
    
    print(f"Attempt {attempt}: You chose {your_turn} and the computer chose {com}.")
    
    # Check if the game is over
    if your_turn == com:
        print(f"You and the computer both chose {com}. It's a tie!")
        break
    elif (your_turn == "rock" and com == "scissors") or \
         (your_turn == "scissors" and com == "paper") or \
         (your_turn == "paper" and com == "rock"):
        print(f"You win! {your_turn} beats {com}.")
        break
    else:
        print(f"You lose! {com} beats {your_turn}.")
        break


    