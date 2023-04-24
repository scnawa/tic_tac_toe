#Create Tic Tac Toe game

def show_board(board):
    print(board[0] + "|" + board[1] + "|" board[2] + "|")
    print(board[3] + "|" + board[4] + "|" board[5] + "|")
    print(board[6] + "|" + board[7] + "|" board[8] + "|")


def check(board, player):
    if  (board[0] == board[1] == board[2]) or
        (board[3] == board[4] == board[5]) or
        (board[6] == board[7] == board[8]) or
        (board[0] == board[3] == board[6]) or
        (board[1] == board[4] == board[7]) or
        (board[2] == board[5] == board[8]) or
        (board[0] == board[4] == board[8]) or
        (board[2] == board[4] == board[6]) or : 
        return True
    else: return False 



def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    winner = False

    while not winner:
        show_board[board]
        move = int(input("Pick a number (1-9) for" + player + ": "))
        if board[move-1] == " ":
            board[move-1] = player
            if check(board, player):
                show_board(board)
                print("Congratulations you win")
                winner = "True"
            elif " " not in board:
                show_board(board)
                print("It's a draw")
                winner = "True"
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"
        else:
            print("Invalid move chose another place")



