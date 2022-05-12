def solve(N, insertCost, removalCost, copyCost):
    dp = [0 for x in range(N+1)]
    dp[1] = insertCost
    for x in range(2, N+1):
        if x % 2 == 0:
            dp[x] = min(dp[x//2]+copyCost, dp[x-1]+insertCost)
        else:
            dp[x] = min(dp[x-1]+insertCost, dp[(x+1)//2]+copyCost+removalCost)
    print(dp)
    return dp[N]

x = solve(9, 1,2,1)
print(x)