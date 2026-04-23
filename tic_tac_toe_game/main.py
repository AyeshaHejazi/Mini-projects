import math

def play_game():
    board = [" " for _ in range(9)]

    def print_board():
        print()
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("--+---+--")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("--+---+--")
        print(board[6] + " | " + board[7] + " | " + board[8])
        print()

    def check_winner(player):
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for c in win_conditions:
            if board[c[0]] == player and board[c[1]] == player and board[c[2]] == player:
                return True
        return False

    def is_draw():
        return " " not in board

    # Minimax Algorithm
    def minimax(is_maximizing):
        if check_winner("O"):
            return 1
        if check_winner("X"):
            return -1
        if is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = minimax(True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    # Best move using minimax
    def best_move():
        best_score = -math.inf
        move = 0

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i

        board[move] = "O"

    # Game loop
    while True:
        print_board()

        try:
            move = int(input("Your move (1-9): ")) - 1
        except:
            print("Invalid input!")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 You win! (IMPOSSIBLE 😳)")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        print("🤖 Computer thinking...")
        best_move()

        if check_winner("O"):
            print_board()
            print("💀 Computer wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break


#  Restart loop
while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Goodbye 👋")
        break