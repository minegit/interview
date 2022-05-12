def solve(A):
    lenA = len(A)
    dp = [0 for x in range(lenA)]
    dp[0] = int(A[0])
    for x in range(1, lenA):
        currentSum = 0
        temp = ""
        for y in range(x, -1, -1):
            temp=A[y]+temp
            currentSum += int(temp)    
        dp[x] = dp[x-1] + currentSum
    print(dp)
    return dp[-1]
print(solve("421"))