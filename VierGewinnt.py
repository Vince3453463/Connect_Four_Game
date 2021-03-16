

board = [["| |", "| |", "| |", "| |", "| |", "| |", "| |"], #6
         ["| |", "| |", "| |", "| |", "| |", "| |", "| |"], #5
         ["| |", "| |", "| |", "| |", "| |", "| |", "| |"], #4
         ["| |", "| |", "| |", "| |", "| |", "| |", "| |"], #3
         ["| |", "| |", "| |", "| |", "| |", "| |", "| |"], #2
         ["| |", "| |", "| |", "| |", "| |", "| |", "| |"]] #1

def hasWon(board):
    #checking rows
    for i in range(6):
        for j in range(4):
            start = board[i][j]
            if (start == "| |"):
                continue
            k = j +1
            count = 1
            while (k < 7): #unnecessary?
                if (board[i][k] == start):
                    count +=1
                    k +=1
                    if (count>=4):
                        return True
                else:
                    break
    #checking columns
    for j in range(6):
        for i in range(5, 2, -1):
            start = board[i][j]
            if (start == "| |"):
                continue
            k = i - 1
            count = 1
            while (k >= 0): # unnecessary?
                if (board[k][j] == start):
                    count +=1
                    k -=1
                    if (count>=4):
                        return True
                else:
                    break
    # checking diagonal upwards
    for i in range(5, 2, -1):
        for j in range(4):
            start = board[i][j]
            if (start == "| |"):
                continue
            k = j +1
            w = i -1
            count = 1
            while (k < 7 and w >= 0): # unnecessary?
                if (board[w][k] == start):
                    count +=1
                    k +=1
                    w -= 1
                    if (count>=4):
                        return True
                else:
                    break
    # checking diagonal downward
    for i in range(3):
        for j in range(4):
            start = board[i][j]
            if (start == "| |"):
                continue
            k = j + 1
            w = i + 1
            count = 1
            while (k < 7 and w < 6): # unnesseray?
                if (board[w][k] == start):
                    count +=1
                    k += 1
                    w += 1
                    if (count>=4):
                        return True
                else:
                    break
    return False
            
def convertRow(row):
    if row == 1:
        return 5
    if row == 2:
        return 4
    if row == 3:
        return 3
    if row == 4:
        return 2
    if row == 5:
        return 1
    if row == 6:
        return 0
    else:
        return -100
    
def printBoard(board):
    for row in board:
        print (' '.join(row) )
    print("\n")

def callPlayer1(board):
    print("your turn, player 1")
    try: 
        row = int(input("Type in row Index: "))
        column = int(input("Type in column Index: "))
    except ValueError:
        print("invalid")
        return callPlayer1(board)
    if (isValid(board, row, column)):
        row = convertRow(row)
        column = column -1
        board[row][column] = "|X|"
        return board
    else:
        print("try again \n")
        return callPlayer1(board)

def callPlayer2(board):
    print("Now you, player 2")
    try:
        row = int(input("Type in row Index: "))
        column = int(input("Type in column Index: "))
    except ValueError:
        print("invalid")
        return callPlayer2(board)
    if (isValid(board, row, column)):
        row = convertRow(row)
        column = column -1
        board[row][column] = "|O|"
        return board
    else:
        print("try again \n")
        return callPlayer2(board)


def isValid(board, row, column):
    row = convertRow(row)
    column = column -1
    if (row < 0 or column < 0 or row >= 6 or column >= 7):
        return False
    if (board[row][column] != "| |"):
        return False
    if(row < 5):
        if(board[row+1][column] == "| |"):
            return False
    return True



#main starts here
          
print("Starting with round 1. Board has 6 rows and 7 columns. Bottom left corner is row = 1, column  = 1")
roundNo = 1
while True:
    print("this is round: " + str(roundNo))
    board = callPlayer1(board)
    printBoard(board)
    if ( hasWon(board)):
        print("Player 1 has won. Magnificient play")
        break
    board = callPlayer2(board)
    printBoard(board)
    if (hasWon(board)):
        print("What a match. Player 2 is victorious")
        break
    roundNo += 1
