def solve(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for x in range(3, n+1):
        dp[x] = dp[x-1]+ dp[x-2]
    
    print(dp[n])


solve(4)
