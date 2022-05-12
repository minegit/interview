def findEmpty(grid, N):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                return row, col
    return None, None
def isValid(num, row, col, grid, N):
    for rows in range(N):
        if grid[rows][col] == num:
            return False
    for cols in range(N):
        if grid[row][cols] == num:
            return False
    modRow = row - row %3
    modCol = col - col %3
    for i in range(3):
        for j in range(3):
            if grid[i+modRow][j+modCol] == num:
                return False
    return True
def solveSudokuUtil(grid, N):
    row, col = findEmpty(grid, N)
    if row is None and col is None:
        return True
    for num in range(1,10):
        if isValid(num, row, col, grid, N):
            grid[row][col] = num
            if solveSudokuUtil(grid, N):
                return True
            else:
                grid[row][col] = 0

if __name__ == "__main__":
    grid = [[0]*9]*9
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    grid = [[0,0,0,4,7,0,0,3,0],
            [0,0,4,0,0,2,0,0,0],
            [0,0,9,5,3,0,0,6,0],
            [5,0,0,0,0,0,4,0,0],
            [0,0,0,0,8,7,9,0,0],
            [0,9,0,0,0,0,6,0,0],
            [0,0,6,0,4,0,0,0,0],
            [8,5,0,0,0,0,0,0,0],
            [0,7,0,0,0,1,2,0,0]]
    solveSudokuUtil(grid, 9)
    print(grid)

