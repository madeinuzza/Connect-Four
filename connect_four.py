board = [
    [" ", " ", " ", " ", " ", " ", " "],  # row 1 (top)
    [" ", " ", " ", " ", " ", " ", " "],  # row 2
    [" ", " ", " ", " ", " ", " ", " "],  # row 3
    [" ", " ", " ", " ", " ", " ", " "],  # row 4
    [" ", " ", " ", " ", " ", " ", " "],  # row 5
    [" ", " ", " ", " ", " ", " ", " "]   # row 6 (bottom)
]


### CREATING THE BOARD 
number_of_columns = 7
number_of_rows = 6
#board = [[]]

for i in range(number_of_rows):
    for j in range(number_of_columns):
        pass


############################ Printing the board ############################
def print_board(board):
    # Column numbers
    print("  1   2   3   4   5   6   7")
    
    # Top border
    print("+---+---+---+---+---+---+---+")
    
    # Each row of the board
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")







############################ Adding pieces to the board ############################

# Player x
def add_piece_to_board_x(column):
    for row in range(number_of_rows, 0, -1):
        if board[row-1][column-1] == " ":
            board[row-1][column-1] = "x"
            return board 

# Player o
def add_piece_to_board_o(column):
#    if board[0][column-1] == "x" or board[0][column-1] == "o":
#        return print(f"The column {column} is already full. Choose a different one.")
        
    if column in range(1, number_of_columns + 1):
        for row in range(number_of_rows, 0, -1):
            if board[row-1][column-1] == " ":
                board[row-1][column-1] = "o"
                return board 





############################ Checking if someone winned ############################

def win_test(board):
    win = False
    
    # testing rows
    for i in range(number_of_rows): # for each row  
        for j in range(number_of_columns - 3): # for each column up to (number_of_columns - 4) + 1
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == "x":
                win = True
                return win
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == "o":
                win = True
                return win


    # testing columns
    for i in range(number_of_columns): # for each column
        for j in range(0, number_of_rows - 3): # for each row up to (number_of_rows - 4) + 1
            if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == "x":
                win = True
                return win
            if board[j][i] == "o" and board[j+1][i] == "o" and board[j+2][i] == "o" and board[j+3][i] == "o":
                win = True
                return win


    # testing diagonals 
    ## \
    for i in range(number_of_rows - 3):
        for j in range(0, number_of_columns -3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == "x":
                win = True
                return win
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == "o":
                win = True
                return win


    ## /
    for i in range(3, number_of_rows):
        for j in range(0, number_of_columns - 3):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == "x":
                win = True
                return win
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == "o":
                win = True
                return win

    return win

############################ empty_space_left test ############################

def empty_space_left_test(board):
    empty_space = False
    for column in board[0]: 
        if column == " ":
            empty_space = True
            break
    return empty_space



############################ Input data (?) ############################


# Connect Four is a game in which the players choose a color and then take turns dropping colored tokens into a six-row, seven-column 
# vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of 
# the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. It is therefore a type of 
# m,n,k-game (7, 6, 4) with restricted piece placement. Connect Four is a solved game; the first player can always win by playing the 
# right moves. 



print("Welcome to Connect Four! \n \n Player X and Player O will take turns dropping their tokens into the grid. \n On your turn, enter the number of the column (1-7) where you want to drop your token. \n The token will fall into the lowest available space in that column. \n \n The first player to connect four tokens in a row (horizontally, vertically, or diagonally) wins the game. \n If the grid fills up before anyone connects four, the game ends in a draw. \n \nLet’s begin!")

print("\n")

print_board(board)

print("\n")

win = False
empty_space_left = True

while win == False and empty_space_left == True:
    
    # Player X
    while True:
        try:
            player_x_column = int(input("Player X, please enter a column: "))
            if 1 <= player_x_column <= 7 and board[0][player_x_column - 1] == " ":
                break 
            else: 
                print("Oops!  That was no valid column.  Try again...")
        except ValueError:
            print("Oops!  That was no valid column.  Try again...")
        
    add_piece_to_board_x(player_x_column)
    print("\n")
    print_board(board)

    empty_space_left = empty_space_left_test(board)
    if empty_space_left == False:
        print("The board is full. It's a tie!")
        break

    print("\n")

    win = win_test(board)
    if win == True:
        print("Congrats Player X, you have won!")
        print("\n")
        break

   # Player O
    while True:
        try:
            player_o_column = int(input("Player O, please enter a column: "))
            if 1 <= player_o_column <= 7 and board[0][player_o_column - 1] == " ":
                break 
            else: 
                print("Oops!  That was no valid column.  Try again...")
        except ValueError:
            print("Oops!  That was no valid column.  Try again...")
        
    add_piece_to_board_o(player_o_column)
    print("\n")
    print_board(board)

    empty_space_left = empty_space_left_test(board)
    if empty_space_left == False:
        print("The board is full. It's a tie!")
        break

    print("\n")

    win = win_test(board)
    if win == True:
        print("Congrats Player O, you have won!")
        print("\n")
        break












