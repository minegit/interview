def lcsRec(X, Y, xIndex, yIndex):
    if xIndex == 0 or yIndex == 0:
        return 0
    elif X[xIndex-1] == Y[yIndex-1]:
        return 1+ lcsRec(X, Y, xIndex-1, yIndex-1)
    else:
        return max(lcsRec(X, Y, xIndex-1, yIndex), lcsRec(X, Y, xIndex, yIndex-1))
def lcsDP(X, Y):
    dp = [[None for x in range(len(Y)+1)] for y in range(len(X)+1)]
    dpc = [["" for x in range(len(Y)+1)] for y in range(len(X)+1)]
    for xIndex in range(len(X)+1):
        for yIndex in range(len(Y)+1):
            if xIndex == 0 or yIndex == 0:
                dp[xIndex][yIndex] = 0
            elif X[xIndex-1] == Y[yIndex-1]:
                dp[xIndex][yIndex] = 1 + dp[xIndex-1][yIndex-1]
                dpc[xIndex][yIndex] =  dpc[xIndex-1][yIndex-1] + X[xIndex-1]
            else:
                if dp[xIndex-1][yIndex] > dp[xIndex][yIndex-1]:
                    dp[xIndex][yIndex]  = dp[xIndex-1][yIndex]
                    dpc[xIndex][yIndex]  = dpc[xIndex-1][yIndex]
                else:
                    dp[xIndex][yIndex]  = dp[xIndex][yIndex-1]
                    dpc[xIndex][yIndex]  = dpc[xIndex][yIndex-1]
    # print(dp)
    # print(dpc)
    return dp[-1][-1],dpc[-1][-1]

X = "MANISH"
Y = "NITISH"
# ans = lcsRec(X, Y, len(X), len(Y))
ansDP = lcsDP(X, Y)
print(ansDP)