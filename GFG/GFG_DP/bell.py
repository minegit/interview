def solve(n):
    dp = [[0 for row in range(n+1)] for col in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][i-1]
        print(dp[i][0])
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            print(dp[i][j], end=" ")
    return dp[n][0]

solve(5)