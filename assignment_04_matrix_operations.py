# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []
    for row_index in range(1, rows + 1):
        row_input = input(f"Enter row {row_index}: ").strip()
        values = row_input.split()
        if len(values) != cols:
            print(f"Error: Expected {cols} values for row {row_index}.")
            return None
        try:
            row = [int(value) for value in values]
        except ValueError:
            print("Error: Please enter valid integer matrix values.")
            return None
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(item).rjust(5) for item in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row_result = []
        for j in range(cols):
            row_result.append(a[i][j] + b[i][j])
        result.append(row_result)
    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            row_result.append(total)
        result.append(row_result)
    return result


def main():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Error: Please enter valid integer dimensions.")
        return

    if rows <= 0 or cols <= 0:
        print("Error: Matrix dimensions must be positive integers.")
        return

    matrix = read_matrix(rows, cols)
    if matrix is None:
        return

    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    print("\nEnter values for the first matrix to add:")
    first_add = read_matrix(rows, cols)
    if first_add is None:
        return
    print("Enter values for the second matrix to add:")
    second_add = read_matrix(rows, cols)
    if second_add is None:
        return

    print("\nSum of matrices:")
    print_matrix(add_matrices(first_add, second_add))

    try:
        rows_b = cols
        cols_b = int(input("\nEnter number of columns for the second matrix to multiply: "))
    except ValueError:
        print("Error: Please enter a valid integer for the number of columns.")
        return

    if cols_b <= 0:
        print("Error: Number of columns must be a positive integer.")
        return

    print(f"Enter values for the second matrix ({cols} x {cols_b}):")
    second_mul = read_matrix(cols, cols_b)
    if second_mul is None:
        return

    print("\nProduct of matrices:")
    print_matrix(multiply_matrices(matrix, second_mul))


if __name__ == "__main__":
    main()

