print("tic tac toe")


player1 = True
valid = True
winner = False


board = list((["", "", ""], ["", "", ""], ["", "", ""]))


def selectTile(x, userInput):
    if(x == 1):
        if(board[0][0] == ""):
            board[0][0] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 2):
        if(board[0][1] == ""):
            board[0][1] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 3):
        if(board[0][2] == ""):
            board[0][2] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 4):
        if(board[1][0] == ""):
            board[1][0] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 5):
        if(board[1][1] == ""):
            board[1][1] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 6):
        if(board[1][2] == ""):
            board[1][2] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 7):
        if(board[2][0] == ""):
            board[2][0] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 8):
        if(board[2][1] == ""):
            board[2][1] = userInput
        else:
            print("Error: Tile already taken")
    if(x == 9):
        if(board[2][2] == ""):
            board[2][2] = userInput
        else:
            print("Error: Tile already taken")    


def checkWinner(board):
    """Check if the current player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False


def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])


while(winner == False):
    printBoard(board)


    userInput = 0


    while(int(userInput) > 9 or int(userInput) < 1):
        print("pick a square 1 - 9: ")
        userInput = input()
       
        if(int(userInput) > 9 or int(userInput) < 1):
            print("Error: value is not between 1 - 9")



    if(player1):
        selectTile(int(userInput), "X")
    else:
        selectTile(int(userInput), "O")


    winner = checkWinner(board)


    if(winner):
        if(player1):
            print("player1 wins!")
            printBoard(board)
        else:
            print("player2 wins!")
            printBoard(board)


    player1 = not player1




