import math

# Nadia's AI Tic Tac Toe Bot (spec)
# I built a simple AI agent that plays the classic game of Tic-Tac-Toe
# against a human player.

# makes empty array[9] the board
board = [' ' for _ in range(9)]

# prints the board according to current array
def print_board():
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
    print()

# checks when board is full (no arrays have value ' ' anymore)
def is_full():
    return ' ' not in board

# checks winnning lines
def win(player):
    complete = [
        (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in complete)

# propogates nodes with initial value
def evaluate():
    if win('O'):
        return 10
    elif win('X'):
        return -10
    else:
        return 0

# Minimax with Alpha-Beta Pruning Function
def minimax(depth, maximizing, alpha, beta):
    score = evaluate()

    # returns current value when recursion hits the leaf node
    if score == 10 or score == -10 or is_full() or depth == 0:
        return score

    # the following is an adaptation of the Alpha-Beta Psuedocode for evaluating
    # moves according to their outcome with (AI winning) being incentivised with
    # adding value to the move and losing leading to a deduction from the moves value
    # https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    if maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                curr = minimax(depth - 1, False, alpha, beta)
                board[i] = ' '
                best = max(best, curr)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break  # leaf comparision (prune)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                curr = minimax(depth - 1, True, alpha, beta)
                board[i] = ' '
                best = min(best, curr)
                beta = min(beta, best)
                if beta <= alpha:
                    break  # leaf comparision (prune)
        return best

# uses minimaximising to make the 'best move'
def ai_move():
    optimal = -math.inf
    curr = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            # initial call (sets bounds)
            move = minimax(depth=9, maximizing=False, alpha=-math.inf, beta=math.inf)
            board[i] = ' '
            if move > optimal:
                optimal = move
                curr = i
    if curr != -1:
        board[curr] = 'O'

# maintains main and loop to prevent incorrect repetiton
# of introduction statement and maintain loop correctly until 'game over'
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!\n")
    print("You are 'X', NadBot is 'O'. Board positions are 0-8.\n")
    print_board()

    while True:
        try:
            move = int(input("Pick your spot 0-8: "))
            if board[move] != ' ':
                print("That spot is taken. Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input. Enter a number from 0 to 8.")
            continue

        board[move] = 'X'
        print_board()

        if win('X'):
            print("You win!")
            break
        elif is_full():
            print("Draw!")
            break

        ai_move()
        print_board()

        if win('O'):
            print("NadBot wins!")
            break
        elif is_full():
            print("Draw!")
            break
    print(" Try again?\n")

