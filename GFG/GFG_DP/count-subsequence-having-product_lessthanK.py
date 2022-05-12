def solveProduct(A, maxProduct):
    n = len(A)
    dp = [[0 for x in range(n+1)] for y in range(maxProduct+1)]
    for product in range(1, maxProduct+1):
        for index in range(1, n+1):
            dp[product][index] = dp[product][index-1]
            if A[index-1] <= product and A[index-1] > 0:
                dp[product][index] += dp[product//A[index-1]][index-1] +1
    
    print(dp)
    return dp[maxProduct][n]

def solveSum(A, maxSum):
    n = len(A)
    dp = [[0 for x in range(n+1)] for y in range(maxSum+1)]
    for sum in range(1, maxSum+1):
        for index in range(1, n+1):
            dp[sum][index] = dp[sum][index-1]
            if A[index-1] <= sum :
                dp[sum][index] += dp[sum-A[index-1]][index-1] +1
    
    print(dp)
    return dp[maxSum][n]

A = [1,2,3,4]
k = 10
print(solveSum(A, k))
