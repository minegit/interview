def solve(A):
    dp = [0 for x in range(len(A))]
    dp[0] = A[0]
    dp[1] = max(A[1], A[0])
    for x in range(2, len(A)):
        dp[x] = max(dp[x-1], A[x]+dp[x-2])
    print(dp)
    return dp[-1]

def solve1(A):
    n =len(A)
    if n ==1:
        return A[0]
    if n == 2:
        return A[1]
    prev = A[0]
    last = A[1]
    maxVal = max(prev, last)
    for x in range(2, n):
        maxVal = max(last, A[x]+prev)
        prev = last
        last = maxVal
    return maxVal
arr = [6, 7, 1, 3, 8, 2, 4]
print(solve1(arr))