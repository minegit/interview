def solve(arr, startIndex, endIndex):
    if startIndex == endIndex:
        return 1
    if arr[startIndex] == arr[endIndex] and endIndex == startIndex+1:
        return 2
    if arr[startIndex] == arr[endIndex]:
        return 2 + solve(arr, startIndex+1, endIndex-1)
    return max(solve(arr, startIndex+1, endIndex), solve(arr, startIndex, endIndex-1))

def solveDp(arr, unusedIndex1, unusedIndex2):
    lenArr = len(arr)
    dp = [[0 for x in range(lenArr)] for y in range(lenArr)]
    for x in range(lenArr):
        dp[x][x] = 1
    for cl in range(2, lenArr+1):
        for i in range(lenArr-cl+1):
            j = i+cl -1
            if arr[i] == arr[j] and cl == 2:
                dp[i][j] = 2
            elif arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]+2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][lenArr-1]
def countPS(arr, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    if startIndex+"."+endIndex in dp:
        return dp[startIndex+"."+endIndex]
    
    if startIndex == endIndex:
        dp[startIndex+"."+endIndex] = 1
        return 1
    
    elif arr[startIndex] == arr[endIndex]:
        return 1 + countPS(arr, startIndex+1, endIndex)+ countPS(arr, startIndex, endIndex-1)
    else:
        return countPS(arr, startIndex+1, endIndex)+ countPS(arr, startIndex, endIndex-1) - countPS(arr, startIndex+1, endIndex-1)

if __name__ == '__main__':
    seq = "GEEKSFORGEEKS"
    n = len(seq)
    dp = dict()
    print("The length of the SolveDP is", solveDp(seq, 0, n - 1),"count is : ",  countPS(seq, 0, n - 1))
