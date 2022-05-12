def solveDP(N, K):
    dp = [0]*(N+1)
    dp[1] = K
    dp[2] = K*K
    for i in range(3, N+1):
        dp[i] = (dp[i-1]+dp[i-2]) * (K-1)
    print(dp)
    return dp[N]

def solve(N, K):
    total = K
    same = 0
    diff = K
    for i in range(2, N+1):
        same = diff
        diff = total * (K-1)
        total = same + diff
        print(same, diff, total)
    return total

x = solveDP(3,9)
print(x)