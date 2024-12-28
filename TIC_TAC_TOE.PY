def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--------")
    print("\n")
    # Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        # Check rows
        if all([cell == player for cell in board[i]]):
            return True
        # Check columns
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (draw condition)
def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to play the Tic-Tac-Toe game
def play_game():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        # Print the board
        print_board(board)

        # Ask for the player's move
        print(f"Player {current_player}'s turn")
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        # Check if the selected cell is empty
        if board[row][col] != ' ':
            print("This cell is already occupied. Please choose another one.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (draw condition)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
        
          