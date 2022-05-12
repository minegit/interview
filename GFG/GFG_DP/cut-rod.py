def solve(priceArr, totalLenOfRod):
    dp = [0] * (totalLenOfRod+1)
    dp[0] = 0
    for eachLen in range(1, totalLenOfRod+1):
        maxPrice = 0
        for elem in range(eachLen):
            maxPrice = max(maxPrice, priceArr[elem]+dp[eachLen-elem-1])
        dp[eachLen] = maxPrice
    
    return dp[totalLenOfRod]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
x = solve(arr, size)
print(x)
