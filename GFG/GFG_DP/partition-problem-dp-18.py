def solve(arr, lenArr, totalSum):
    if totalSum == 0:
        return True
    if totalSum > 0 and lenArr == 0:
        return False
    if arr[lenArr-1] > totalSum:
        return solve(arr, lenArr-1, totalSum)
    return solve(arr, lenArr-1, totalSum) or solve(arr, lenArr-1, totalSum-arr[lenArr-1])

def solveDp(arr, lenArr, totalSum):
    dp = [[False] * (totalSum+1)]*(lenArr+1)
    for elemrange in range(lenArr+1):
        dp[elemrange][0] = True
    for sumRange in range(totalSum+1):
        dp[0][sumRange] = False
    for elem in range(1, lenArr+1):
        for subsetSum in range(1, totalSum+1):
            if subsetSum < arr[elem-1]:
                dp[elem][subsetSum] = dp[elem-1][subsetSum]
            else:
                dp[elem][subsetSum] = dp[elem-1][subsetSum] or dp[elem-1][subsetSum-arr[elem-1]]
    return dp[lenArr][totalSum]

arr = [1,5,5,11,2]
totalSum = sum(arr)
if totalSum %2 == 0:
    ispossible  = solve(arr, len(arr), totalSum//2)
    if ispossible:
        print("POSSIBLE")
    else:
        print("NOT POSSIBLE")
else:
    print("NOT POSSIBLE")
