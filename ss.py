import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3] + ' | ' + board[i*3+1] + ' | ' + board[i*3+2])
        if i < 2:
            print('--+---+--')
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw():
    return ' ' not in board

# Minimax with Alpha-Beta Pruning
def minimax(is_maximizing, ai_player, human_player, alpha, beta):
    if check_winner(ai_player): return 1
    if check_winner(human_player): return -1
    if is_draw(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(False, ai_player, human_player, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = human_player
                score = minimax(True, ai_player, human_player, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def best_move(ai_player, human_player):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_player
            score = minimax(False, ai_player, human_player, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = ai_player

def play_game():
    print("Welcome to Tic Tac Toe!")

    human_player = input("Do you want to be X or O? ").upper()
    while human_player not in ['X', 'O']:
        human_player = input("Invalid choice! Please choose X or O: ").upper()

    ai_player = 'O' if human_player == 'X' else 'X'
    print(f"You are {human_player}, AI is {ai_player}.")
    print_board()

    if ai_player == 'X':
        print("AI is making the first move...")
        best_move(ai_player, human_player)
        print_board()

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = human_player
        print_board()

        if check_winner(human_player):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("AI is making a move...")
        best_move(ai_player, human_player)
        print_board()

        if check_winner(ai_player):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
