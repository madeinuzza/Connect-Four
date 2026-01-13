**🎮 Connect Four (Python Console Game)**

A simple console-based implementation of the classic Connect Four game, written in Python. Two players take turns dropping tokens into a 6×7 grid, aiming to connect four pieces in a row before their opponent.


**📌 Overview**

This project recreates the classic Connect Four game in the terminal.
Players X and O alternate turns, selecting a column where their token will fall to the lowest available position. The game automatically checks for wins and draws after every move.


**🕹 Game Rules**

The board has 6 rows and 7 columns
Player X always goes first
On your turn, enter a column number from 1 to 7
Tokens fall to the lowest available space in the chosen column
A player wins by connecting four tokens:
  - Horizontally
  - Vertically
  - Diagonally
If the board fills up without a winner, the game ends in a draw


**✨ Features**

1. Input validation for incorrect or full columns
2. Gravity-based token placement
3. Automatic win detection:
    - Horizontal
    - Vertical
    - Diagonal (\ and /)
4. Draw detection when no empty spaces remain


**🧱 Board Representation**

- The game board is represented as a 2D list:
  
board = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]

- " " → empty cell
- "x" → Player X
- "o" → Player O


**🧩 Functions**

1. print_board(board)
Prints the current state of the board with column numbers and borders.

2. add_piece_to_board_x(column)
Drops an "x" token into the selected column for Player X.

3. add_piece_to_board_o(column)
Drops an "o" token into the selected column for Player O.

4. win_test(board)
Checks for a winning condition in:
  - Rows
  - Columns
  - Diagonals
Returns True if a player has won, otherwise False.

5. empty_space_left_test(board)
Checks if there is still at least one empty space in the board.
Used to determine a draw.


**▶️ How to Run**

1. Ensure Python 3 is installed
2. Clone the repository or copy the code into a file:
    git clone <repository-url>
    cd connect-four
3. Run the game:
    python connect_four.py
4. Follow the prompts and enter a column number (1–7) when asked
