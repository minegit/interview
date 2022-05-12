def solve(A, n):
    dp = [0] * n
    dp[n-1] = 1
    for i in range(n-2, -1, -1):
        mxm = 0
        for j in range(i+1, n):
            if A[i] % A[j] == 0 or A[j] % A[i] == 0:
                mxm = max(mxm, dp[j])
        dp[i] = 1 + mxm
    return max(dp)

A = [ 1, 3, 6, 13, 17, 18 ]
n = len(A)

x = solve(A, n)
print(x)