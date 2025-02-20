def print_board(board):
    """Print the current state of the board"""
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

def check_winner(board):
    """Check if there's a winner"""
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    
    if " " not in board:
        return "Tie"
    
    return None

def is_valid_move(board, position):
    """Check if the move is valid"""
    return 1 <= position <= 9 and board[position-1] == " "

def play_game():
    """Main game function"""
    board = [" " for _ in range(9)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Enter numbers 1-9 to make your move:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("\nLet's begin!\n")
    
    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        try:
            position = int(input("Enter position (1-9): "))
            if not is_valid_move(board, position):
                print("Invalid move! Try again.")
                continue
                
            board[position-1] = current_player
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "Tie":
                    print("\nGame Over! It's a tie!")
                else:
                    print(f"\nGame Over! Player {winner} wins!")
                break
                
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Please enter a number between 1 and 9!")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break