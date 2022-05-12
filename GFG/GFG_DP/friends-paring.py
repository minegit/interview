def solve(N):
    if N <= 2:
        return N
    return solve(N-1) + solve(N-2) * (N-1) 

def solveDp(N):
    if N <= 2:
        return N
    dp = [0 for x in range(N+1)]
    for x in range(N+1):
        if x <=2:
            dp[x] = x
        else:
            dp[x] = dp[x-1] + dp[x-2] * (x-1)
        print(dp)
    return dp[N]
x = solveDp(5)
print(x)
    