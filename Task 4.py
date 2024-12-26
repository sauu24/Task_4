def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_safe(grid, row, col, num):
    # Check if 'num' is not in the given row
    if num in grid[row]:
        return False

    # Check if 'num' is not in the given column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if 'num' is not in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # Backtrack
            grid[row][col] = 0

    return False

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

# Input: 9x9 Sudoku grid with 0 as empty cells
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Input Sudoku Grid:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku Grid:")
    print_grid(sudoku_grid)
else:
    print("\nNo solution exists")
