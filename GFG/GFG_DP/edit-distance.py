def solve(X, Y, lenX, lenY):
    dp  = [[0 for x in range(lenX+1)] for Y in range(lenY+1)]
    for yIndex in range(lenY+1):
        for xIndex in range(lenX+1):
            if yIndex == 0:
                dp[yIndex][xIndex] = xIndex
            elif xIndex == 0:
                dp[yIndex][xIndex] = yIndex
            elif X[xIndex-1] == Y[yIndex-1]:
                dp[yIndex][xIndex] = dp[yIndex-1][xIndex-1]
            else:
                dp[yIndex][xIndex] = 1 + min (dp[yIndex-1][xIndex], dp[yIndex][xIndex-1],dp[yIndex-1][xIndex-1])
    return dp[lenY][lenX]
    