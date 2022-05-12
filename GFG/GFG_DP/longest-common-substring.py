def solve(X, Y):
    lenX = len(X)
    lenY = len(Y)
    dp = [[None for y in range(lenY+1)] for x in range(lenX+1)]
    maxVal = 0
    for xIndex in range(lenX+1):
        for yIndex in range(lenY+1):
            if xIndex == 0 or yIndex == 0:
                dp[xIndex][yIndex] = 0
            elif X[xIndex-1] == Y[yIndex-1]:
                dp[xIndex][yIndex] = 1 + dp[xIndex-1][yIndex-1]
                maxVal = max(maxVal, dp[xIndex][yIndex])
            else:
                dp[xIndex][yIndex] = 0
    print(dp)
    return maxVal

def LCSubStr(X, Y, m, n):
 
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.
 
    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
 
    # To store the length of
    # longest common substring
    result = 0
 
    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result
 
 
# Driver Code
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
X = 'MANISH'
Y = 'NITISH'
X = 'sbsbsdsdsdsdsdadafafafafafb'
Y = 'sasasdsdsdsdsdbdbfbfafafafa'
 
m = len(X)
n = len(Y)
 
print('Length of Longest Common Substring is',
      LCSubStr(X, Y, m, n))
X = 'bbbaaasdfddsdfsasfdsasdffas'
Y = 'sasasdsdsdsdsdbdbfbfafafafa'
# print(solve(X, Y))