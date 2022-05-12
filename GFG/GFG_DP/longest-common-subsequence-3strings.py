def lcsRec(X, Y,Z,  xIndex, yIndex, zIndex):
    if xIndex == 0 or yIndex == 0 or zIndex == 0:
        return 0
    elif X[xIndex-1] == Y[yIndex-1] and Y[yIndex-1] == Z[zIndex-1]:
        return 1+ lcsRec(X, Y, xIndex-1, yIndex-1, zIndex-1)
    else:
        return max(lcsRec(X, Y, xIndex-1, yIndex, zIndex), lcsRec(X, Y, xIndex, yIndex-1, zIndex),lcsRec(X, Y, xIndex, yIndex, zIndex-1))

def lcsDP(X, Y, Z):
    dp = [[[0 for z in range(len(Z)+1)] for x in range(len(Y)+1)] for y in range(len(X)+1)]
    # dpc = [[["" for z in range(len(Z)+1)] for x in range(len(Y)+1)] for y in range(len(X)+1)]
    for xIndex in range(len(X)+1):
        for yIndex in range(len(Y)+1):
            for zIndex in range(len(Z)+1):
                if xIndex == 0 or yIndex == 0 or zIndex == 0:
                    dp[xIndex][yIndex][zIndex] = 0
                elif X[xIndex-1] == Y[yIndex-1] and X[xIndex-1] == Z[zIndex-1]:
                    dp[xIndex][yIndex][zIndex] = 1 + dp[xIndex-1][yIndex-1][zIndex-1]
                    # dpc[xIndex][yIndex][zIndex] =  dpc[xIndex-1][yIndex-1][zIndex-1] + X[xIndex-1]
                else:
                    dp[xIndex][yIndex][zIndex] = max(dp[xIndex-1][yIndex][zIndex],dp[xIndex][yIndex-1][zIndex],dp[xIndex][yIndex][zIndex-1])
                    # if dp[xIndex-1][yIndex][zIndex] > dp[xIndex][yIndex-1][zIndex] and dp[xIndex-1][yIndex][zIndex] > dp[xIndex][yIndex][zIndex-1]:
                    #     dp[xIndex][yIndex][zIndex]  = dp[xIndex-1][yIndex][zIndex]
                    #     # dpc[xIndex][yIndex][zIndex]  = dpc[xIndex-1][yIndex][zIndex]
                    # elif dp[xIndex][yIndex-1][zIndex] > dp[xIndex-1][yIndex][zIndex] and dp[xIndex][yIndex-1][zIndex] > dp[xIndex][yIndex][zIndex-1]:
                    #     dp[xIndex][yIndex][zIndex]  = dp[xIndex][yIndex-1][zIndex]
                    #     # dpc[xIndex][yIndex][zIndex]  = dpc[xIndex][yIndex-1][zIndex]
                    # elif dp[xIndex][yIndex][zIndex-1] > dp[xIndex-1][yIndex][zIndex] and dp[xIndex][yIndex][zIndex-1] > dp[xIndex][yIndex-1][zIndex]:
                    #     dp[xIndex][yIndex][zIndex]  = dp[xIndex][yIndex][zIndex-1]
                    #     # dpc[xIndex][yIndex][zIndex]  = dpc[xIndex][yIndex][zIndex-1]
    print(dp)
    # print(dpc)
    return dp[-1][-1][-1]

X = 'AGGT12'
Y = '12TXAYB'
Z = '12XBA'
# ans = lcsRec(X, Y, len(X), len(Y))
ansDP = lcsDP(X, Y, Z)
print(ansDP)