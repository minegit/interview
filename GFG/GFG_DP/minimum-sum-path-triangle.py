def solve(A):
    lenA = len(A)-1
    dp = [[None] * (lenA+1) for x in range(lenA+1)]
    for row in range(lenA, -1, -1):
        for col in range(0,row+1):
            if row == lenA:
                dp[row][col] = A[row][col]
            else:
                dp[row][col] = A[row][col]+min(dp[row+1][col], dp[row+1][col+1])
        print(dp)
    return dp[0][0]

def solveOnSpace(A):
    lenA = len(A)-1
    dp = [None] * (lenA+1)
    for row in range(lenA, -1, -1):
        for col in range(0,row+1):
            if row == lenA:
                dp[col] =A[row][col]
            else:
                dp[col] = A[row][col]+min(dp[col], dp[col+1])
        print(dp)
    return dp[0]

A = [ [ 2 ], [ 3, 9 ], [ 1, 6, 7 ] ];

print(solveOnSpace(A))
