def isSafe(move, A, N, maze):
    x, y = move
    if x >= 0 and y>= 0 and x<N and y<N and A[x][y] == 1 and maze[x][y] == -1:
        return True
    return False

def solveMaze(A, N, maze, pos, x, y):
    if x == N-1 and y == N -1:
        return True
    nextMove = [(x, y+1), (x+1, y),(x-1,y), (x,y-1)]
    for move in nextMove:
        if isSafe(move, A, N, maze) and maze[move[0]][move[1]] != 0:
            maze[move[0]][move[1]] = pos
            if solveMaze(A, N, maze, pos+1, move[0], move[1]):
                return True
            maze[move[0]][move[1]] = 0

def solve(A, N):
    maze = [[-1 for x in range(N)] for y in range(N)]
    pos = 1
    maze[0][0] = pos
    if solveMaze(A, N, maze, pos+1, 0, 0):
        print(maze)
    else:
        print(None)

if __name__ == "__main__":
    # Initialising the maze
    maze = [ [1, 1, 1, 0],
             [1, 1, 1, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
              
    solve(maze, 4)