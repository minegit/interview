def solve(A):
    lenA = len(A)
    dp = [1] * lenA
    for x in range(1, lenA):
        for y in range(x):
            if A[x] > A[y] and dp[x] < dp[y]+1:
                dp[x] = dp[y]+1
    
    print(dp)
    return max(dp)

def solveBi(A):
    lenA = len(A)
    dp = [1] * lenA
    dpDecreasing = [1] * lenA
    for x in range(1, lenA):
        for y in range(x):
            if A[x] > A[y] and dp[x] < dp[y]+1:
                dp[x] = dp[y]+1
    for x in range(lenA-2, -1, -1):
        for z in range(lenA-1, x, -1):
            if A[x] > A[z] and dpDecreasing[x] < dpDecreasing[z]+1:
                dpDecreasing[x] = dpDecreasing[z]+1
    print(dp)
    print(dpDecreasing)
    maxV  = dp[0] + dpDecreasing[0] -1
    for i in range(lenA):
        maxV = max(maxV, dp[i]+dpDecreasing[i]-1)
    return maxV

def solveBiSum(A):
    lenA = len(A)
    dp =A[:]
    dpDecreasing = A[:]
    for x in range(1, lenA):
        for y in range(x):
            if A[x] > A[y] and dp[x] < dp[y] + A[x]:
                dp[x] = dp[y] + A[x]
    for x in range(lenA-2, -1, -1):
        for z in range(lenA-1, x, -1):
            if A[x] > A[z] and dpDecreasing[x] < dpDecreasing[z] + A[x]:
                dpDecreasing[x] = dpDecreasing[z]+A[x]
    print(dp)
    print(dpDecreasing)
    maxV  = dp[0] + dpDecreasing[0] -A[0]
    for i in range(lenA):
        maxV = max(maxV, dp[i]+dpDecreasing[i]-A[i])
    return maxV

def solveBiProduct(A):
    lenA = len(A)
    dp =A[:]
    dpDecreasing = A[:]
    for x in range(1, lenA):
        for y in range(x):
            if A[x] > A[y] and dp[x] < (dp[y] * A[x]):
                dp[x] = dp[y] * A[x]
    for x in range(lenA-2, -1, -1):
        for z in range(lenA-1, x, -1):
            if A[x] > A[z] and dpDecreasing[x] < (dpDecreasing[z] * A[x]):
                dpDecreasing[x] = dpDecreasing[z]*A[x]
    print(dp)
    print(dpDecreasing)
    maxV  = 0
    for i in range(lenA):
        maxV = max(maxV, dp[i]+(dpDecreasing[i]/A[i]))
    return maxV

    
    

# A = [10, 22, 9, 33, 21, 50, 41, 60]

# A = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]

# A = [1, 11, 2,10, 4, 5, 2, 1]

A = [1, 15, 51, 45, 33, 100, 12, 18, 9]
x = solveBiSum(A)
print(x)