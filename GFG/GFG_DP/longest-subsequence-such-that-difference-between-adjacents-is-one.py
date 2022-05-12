def solve(A):
    lenA = len(A)
    dp = [1] * lenA
    for index in range(1,lenA):
        for subIndex in range(index):
            if abs(A[index] -A[subIndex]) <= 1 and dp[index] < dp[subIndex] +1:
                dp[index] = dp[subIndex] +1
    print(dp)
    return max(dp)

def solvePrefix(A, I, K):
    lenA = (I+1)
    dp = [1] * lenA
    for index in range(1,lenA):
        for subIndex in range(index):
            if A[index]>A[subIndex] and A[index]<A[K] and dp[index] < dp[subIndex] +A[index]:
                dp[index] = dp[subIndex] +A[index]
    print(dp)
    return max(dp)+A[K]

A = [1, 2, 3, 2, 3, 7, 2, 1]
A = [1, 101, 2, 3, 100, 4, 5]
print(solvePrefix(A, 4, 6))