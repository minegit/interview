class Node():
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    def __repr__(self) -> str:
        return f"""r:{self.row} c:{self.col}"""

def process_right(row, col, A, rottenQ):
    if A[row][col+1] == 1:
        rottenQ.append(Node(row, col+1))
        A[row][col+1] = 2
def process_left(row, col, A, rottenQ):
    if A[row][col-1] ==1:
        rottenQ.append(Node(row, col-1))
        A[row][col-1] =2
def process_above(row, col, A, rottenQ):
    if A[row-1][col] == 1:
        rottenQ.append(Node(row-1, col))
        A[row-1][col] = 2
def process_below(row, col, A, rottenQ):
    if A[row+1][col] == 1:
        rottenQ.append(Node(row+1, col))
        A[row+1][col] = 2

def insert_nearby_Orange(rotOrange, rottenQ, A, totalRow, totalCol):
    row = rotOrange.row
    col = rotOrange.col
    if row == 0:
        if col == 0:
            process_right(row, col, A, rottenQ)
        elif col == totalCol-1:
            process_left(row, col, A, rottenQ)
        else:
            process_right(row, col, A, rottenQ)
            process_left(row, col, A, rottenQ)
        process_below(row, col, A, rottenQ)

    elif row == totalRow-1:
        if col == 0:
            process_right(row, col, A, rottenQ)
        elif col == totalCol-1:
            process_left(row, col, A, rottenQ)
        else:
            process_right(row, col, A, rottenQ)
            process_left(row, col, A, rottenQ)
        process_above(row, col, A, rottenQ)
    elif col == 0:
        process_right(row, col, A, rottenQ)
        process_below(row, col, A, rottenQ)
    elif col == totalCol-1:
        process_left(row, col, A, rottenQ)
        process_below(row, col, A, rottenQ)
    else:
        process_right(row, col, A, rottenQ)
        process_left(row, col, A, rottenQ)
        process_above(row, col, A, rottenQ)
        process_below(row, col, A, rottenQ)
    
def solve(A):
    nrows = len(A)
    ncols = len(A[0])
    rottenQ = []
    for row in range(nrows):
        for col in range(ncols):
            if A[row][col] == 2:
                rottenQ.append(Node(row,col))
    h = -1
    while True:
        rottenCount = len(rottenQ)
        if rottenCount == 0:
            break 
        h+=1
        while rottenCount > 0:
            rotOrange = rottenQ.pop(0)
            insert_nearby_Orange(rotOrange, rottenQ, A, nrows, ncols)
            rottenCount-=1
    
    for row in range(nrows):
        for col in range(ncols):
            if A[row][col] == 1:
                return -1
    return h

A = [[2, 1, 0, 2, 1],
         [0, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
print(solve(A))



