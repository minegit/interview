INF = 1000000
def solve(A, lenA, totalWt):
    costArr = list()
    wtArr = list()
    size = 0
    for i in range(lenA):
        if A[i] != -1:
            costArr.append(A[i])
            wtArr.append(i+1)
            size+=1
    dp = [[0 for x in range(totalWt+1)] for y in range(size+1)]
    for x in range(totalWt+1):
        dp[0][x] = INF
    for x in range(1, size+1):
        dp[x][0] = 0
    
    for index in range(1, size+1):
        for eachWt in range(1, totalWt+1):
            if wtArr[index-1] > eachWt:
                dp[index][eachWt] = dp[index-1][eachWt]
            else:
                dp[index][eachWt] = min(costArr[index-1]+dp[index][eachWt-wtArr[index-1]],
                                             dp[index-1][eachWt])
    if dp[size][totalWt] == INF:
        return -1
    return dp[size][totalWt]

