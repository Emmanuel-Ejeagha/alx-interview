#!/usr/bin/python3

"""Learn about the n queens problem and how to solve it"""
import sys

args = sys.argv
if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

n = args[1]
try:
    N = int(n)
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

matrix = [[0] * N for _ in range(N)]


def valid_row(row):
    """Validate a row that a queen can be placed"""
    return sum(row) == 0


def valid_column(index, matrix):
    """Validate a column that a queen can be placed"""
    for row in matrix:
        if row[index] == 1:
            return False
    return True


def valid_diagonal(mat, row, col):
    """Validate a diagonal that a queen can be placed"""

    for m in range(N):
        if (mat[row][m] == 1) or (mat[m][col] == 1):
            return False

    for k in range(N):
        for j in range(N):
            if (k - j == row - col) or (k + j == row + col):
                if mat[k][j] == 1:
                    return False
    return True


def get_index(arr):
    """Get index of position 1"""
    i = 0
    while i < N:
        if arr[i] == 1:
            return i
        i += 1
    return -1


def print_matrix(matrix):
    """Print the positions of the n queen solution"""
    index = []
    for idx, row in enumerate(matrix):
        index.append([idx, get_index(row)])
    print(index)


def generate_solutions(col, matrix, solutions):
    """Generate solutions for the N queens problem"""
    if col >= N:
        solutions.append([row[:] for row in matrix])
        return

    for i in range(N):
        if valid_column(col, matrix) and valid_row(
                matrix[i]) and valid_diagonal(matrix, i, col):

            matrix[i][col] = 1

            generate_solutions(col + 1, matrix, solutions)
            matrix[i][col] = 0


if __name__ == '__main__':
    solutions = []
    generate_solutions(0, matrix, solutions)

    for solution in solutions:
        print_matrix(solution)
