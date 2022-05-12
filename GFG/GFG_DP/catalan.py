def solve(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    for x in range(2, n + 1):
        for y in range(x):
            dp[x] += dp[y] * dp[n-y-1]
    return dp[-1]
solve(10)