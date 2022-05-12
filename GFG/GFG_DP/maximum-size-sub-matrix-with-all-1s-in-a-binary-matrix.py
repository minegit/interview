def solve(A):
    nRow, nCol = len(A), len(A[0])
    dp = [[0 for x in range(nCol)] for y in range(nRow)]

    for x in range(0, nCol):
        dp[0][x] = A[0][x]
    for y in range(1, nRow):
        dp[y][0] = A[y][0]
    
    for row in range(1, nRow):
        for col in range(1, nCol):
            if A[row][col] == 1:
                dp[row][col] = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1])+1
            else:
                dp[row][col] = 0
    # print(dp)
    maxSize = 0
    maxRow, maxCol = 0,0
    for row in range(0, nRow):
        for col in range(0, nCol):
            if dp[row][col] > maxSize:
                maxSize = dp[row][col]
                maxRow, maxCol = row, col
    
    for row in range(maxSize-1, -1, -1):
        for col in range(maxSize-1, -1, -1):
            print("("+str(maxRow-row)+"," +str(maxCol-col)+")", end=" ")
        print("")

A = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]];
solve(A)

