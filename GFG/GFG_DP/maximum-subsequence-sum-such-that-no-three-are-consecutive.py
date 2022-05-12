def solve(A):
    n = len(A)
    if n <= 2:
        return sum(A)
    dp = [0] * (n)
    dp[0] = A[0]
    dp[1] = A[0]+A[1]
    dp[2] = max(dp[1], dp[2], dp[1]+dp[2])
    for index in range(3, n):
        dp[index] = max(dp[index-1], dp[index]+A[index-2], A[index]+A[index-1]+dp[index-3])
    print(dp)
    return dp[n-1]

A = [1, 2, 3, 4, 5, 6, 7, 8]
print(solve(A))