#!/usr/bin/python3
"""N queens"""
import sys

# Check if the number of arguments is correct
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Check if N is a number
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Check if N is even and at least 6
if n % 2 == 0 and n < 6:
    print("N must be at least 6 if it is even")
    sys.exit(1)

# Check if N is odd and at least 5
if n % 2 == 1 and n < 5:
    print("N must be at least 5 if it is odd")
    sys.exit(1)


# A helper function to check if a queen can be placed in a given position
def is_valid(board, row, col):
    """check if a queen can be placed in a given position"""
    n = len(board)
    # Check if there is already a queen in the same column
    for i in range(n):
        if board[i][col] == "Q":
            return False
    # Check if there is already a queen in the same row
    for j in range(n):
        if board[row][j] == "Q":
            return False
    # Check if there is already a queen in the same diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    return True

# A recursive function to solve the N Queens problem
def solve(board, row):
    """ solve the N Queens problem"""
    n = len(board)
    # Base case: all queens have been placed
    if row == n:
        print(" ".join(board[i]) for i in range(n))
        return
    # Try to place a queen in each column of the current row
    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = "Q"
            solve(board, row + 1)
            board[row][col] = "."


# Initialize the board
board = [["."] * n for _ in range(n)]

# Call the solve function with the initial board and the first row
solve(board, 0)

