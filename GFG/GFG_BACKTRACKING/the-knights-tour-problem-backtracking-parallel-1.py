def isSafe(x, y, board, totalRow, totalCol):
    if x>= 0 and y >= 0 and x< totalRow and y < totalCol and board[x][y] == -1:
        return True
    return False

def solveKtUtil(N, board, move_x,move_y, curr_x, curr_y, pos):
    if pos == (N*N):
        return True
    for x in range(8):
        next_x = curr_x+move_x[x]
        next_y = curr_y+move_y[x]
        if isSafe(next_x, next_y, board, N, N):
            board[next_x][next_y] = pos
            if solveKtUtil(N, board, move_x, move_y, next_x, next_y, pos+1):
                return True
            board[next_x][next_y] = -1
    return False
from multiprocessing import Pool
def solveKt(N):
    initArr = []
    for row in range(N):
        for col in range(N):
            initArr.append((row, col, N))
    with Pool(processes=8) as pool:
        pool.map(solveThis, initArr)

def solveThis(data):
    row, col, N = data
    board = [[-1 for i in range(N)]for j in range(N)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[row][col] = 0
    pos = 1
    if not solveKtUtil(N, board, move_x, move_y, 0,0,pos):
        print(None)
    else:
        print(board)

# solveKt(8)

def f(x):
    row, col, N = x
    print(row, col, N)

def x1(N):
    initArr = []
    for row in range(N):
        for col in range(N):
            initArr.append((row, col, N))
    with Pool(processes=4) as pool:
        pool.map(f, initArr)

if __name__ == '__main__':
    solveKt(8)


