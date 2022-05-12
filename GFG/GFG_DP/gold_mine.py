def solve(gold, nrow, ncol):
    dp = [[0 for i in range(ncol)] for j in range(nrow)]
    dpPath = [[" " for i in range(ncol)] for j in range(nrow)]
    # for x in range(row):
    #     dp[x][0] = 1
    # for y in range(col):
    #     dp[0][y] = 2
    # print(dp)
    for col in range(ncol-1, -1, -1):
        for row in range(nrow):
            dpPath[row][col]  = "(" + str(row)+ "," + str(col) + ")"
            if col == ncol -1:
                rightGold = 0
            else:
                rightGold = dp[row][col+1]
            if row ==0 or col == ncol -1:
                rightUpGOld = 0
            else:
                rightUpGOld = dp[row-1][col+1]
            if row == nrow-1 or col == ncol -1:
                rightDownGold = 0
            else:
                rightDownGold = dp[row+1][col+1]
            dp[row][col] =gold[row][col] + max(rightGold,rightUpGOld,rightDownGold)
            if col != ncol -1:
                if rightGold >= rightUpGOld and rightGold >= rightDownGold:
                    dpPath[row][col]  = "(" + str(row)+ "," + str(col) + ")" + "->" + dpPath[row][col+1]
                if rightUpGOld >= rightGold and rightUpGOld >= rightDownGold:
                    dpPath[row][col]  = "(" + str(row)+ "," + str(col) + ")" + "->" + dpPath[row-1][col+1]
                if row >0 and rightDownGold >= rightUpGOld and rightDownGold >= rightGold:
                    dpPath[row][col]  = "(" + str(row)+ "," + str(col) + ")" + "->" + dpPath[row+1][col+1]
            

    maxValue = dp[0][0]
    for x in range(row):
        maxValue = max(maxValue, dp[x][0])
    print( maxValue )
    print(dpPath)
gold = [[1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]]

solve(gold, 4, 4)