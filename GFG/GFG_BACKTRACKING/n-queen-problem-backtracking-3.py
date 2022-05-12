def placedQueen(x, y, board, N):
    for row in range(N):
        if board[row][y] == 1:
            return False
    for col in range(N):
        if board[x][col] == 1:
            return False
    for row , col in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[row][col] == 1:
            return False
    for row , col in zip(range(x, N, 1), range(y, -1, -1)):
        if board[row][col] == 1:
            return False
    for row , col in zip(range(x, N, 1), range(y, N, 1)):
        if board[row][col] == 1:
            return False
    for row , col in zip(range(x, -1, -1), range(y, N, 1)):
        if board[row][col] == 1:
            return False
    return True

def isQueenPlaced(board, col, N):
    if col >= N:
        return True
    for row in range(N):
        if placedQueen(row, col, board, N):
            board[row][col] = 1
            if isQueenPlaced(board, col+1, N):
                return True
            board[row][col] = 0
    return False




def solveNQ(N):
    board = [[0 for x in range(N)]for y in range(N)]
    if isQueenPlaced(board, 0, N):
        print(board)
    else:
        print(None)

solveNQ(8)