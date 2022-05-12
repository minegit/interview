def solveRecur(A, currentRow, totalRow, currentCol, totalCol, dp):
    if(dp[currentRow][currentCol] != -1):
        return dp[currentRow][currentCol]
    if currentRow == totalRow and currentCol == totalCol:
        dp[currentRow][currentCol] = 0
        return 0
    downMove , rightMove = False, False
    if currentCol == totalCol:
        if abs(A[currentRow][currentCol]-A[currentRow+1][currentCol]) == 1:
            dp[currentRow][currentCol] = 1+solveRecur(A, currentRow+1, totalRow, currentCol, totalCol, dp)
        else:
            dp[currentRow][currentCol] = 0
        return dp[currentRow][currentCol]
    if currentRow == totalRow:
        if abs(A[currentRow][currentCol] - A[currentRow][currentCol+1]):
            dp[currentRow][currentCol] = 1+solveRecur(A, currentRow, totalRow, currentCol+1, totalCol, dp)
        else:
            dp[currentRow][currentCol] = 0
        return dp[currentRow][currentCol]
    if abs(A[currentRow][currentCol]-A[currentRow+1][currentCol]) == 1:
        downMove = True
    if abs(A[currentRow][currentCol] - A[currentRow][currentCol+1]) == 1:
        rightMove = True
    if downMove and rightMove : 
        dp[currentRow][currentCol] = 1 + max(solveRecur(A, currentRow+1, totalRow, currentCol, totalCol, dp), 
                        solveRecur(A, currentRow, totalRow, currentCol+1, totalCol, dp))
        return dp[currentRow][currentCol]
    if downMove:
        dp[currentRow][currentCol] =  1+solveRecur(A, currentRow+1, totalRow, currentCol, totalCol, dp)
        return dp[currentRow][currentCol]
    if rightMove:
        dp[currentRow][currentCol] =  1+solveRecur(A, currentRow, totalRow, currentCol+1, totalCol, dp)
        return dp[currentRow][currentCol]
    dp[currentRow][currentCol] = 0
    return 0
# dp = [[-1 for x in range(4)] for y in range(4)]
arr = [[9,6,5,2],[8,7,6,5],[7,3,1,6],[1,1,1,7]]
# x = solveRecur(arr, 0, 3, 0, 3, dp)
# print(x)
def solve(A, row, col):
    dp = [[-1 for x in range(col+1)] for y in range(row+1)]
    for rowItem in range(row+1):
        for colItem in range(col+1):
            if(dp[rowItem][colItem] == -1):
                dp[rowItem][colItem] = solveRecur(arr, rowItem, 3, colItem, 3, dp)
    print(dp)
    return max(max(dp))
x = solve(arr, 3, 3)
print(x)