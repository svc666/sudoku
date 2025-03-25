from flask import Flask, jsonify
import random

app = Flask(__name__)

# Function to generate a 9x9 Sudoku grid
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_diagonal_boxes(board)
    solve_sudoku(board)
    remove_numbers(board, 40)  # Remove 40 numbers to make it a puzzle
    return board

# Function to fill diagonal 3x3 boxes
def fill_diagonal_boxes(board):
    for i in range(0, 9, 3):
        fill_box(board, i, i)

# Function to fill a 3x3 box
def fill_box(board, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = nums.pop()

# Sudoku solver
def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    box_start_row, box_start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + box_start_row][j + box_start_col] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return

