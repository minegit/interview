def solve(coeffArr, start, end, rhs):
    if rhs == 0:
        return 1
    result = 0
    for i in range(start, end+1):
        if coeffArr[i]<= rhs :
            result += solve(coeffArr, i, end, rhs-coeffArr[i])
    return result

def solvedp(coeffArr, rhs):
    n = len(coeffArr)
    dp = [0 for x in range(rhs+1)]
    dp[0] = 1
    for coeff in range(n):
        for j in range(coeffArr[coeff], rhs+1):
            dp[j] += dp[j-coeffArr[coeff]]
    return dp[rhs]

coeffArr = [2, 2, 5]
rhs = 4


def sol1(X):
    xlen = len(X)
    dp = [0 for i in range(xlen+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, xlen+1):
        dp[i] = dp[i-1]+(i-1)*dp[i-2]
print(solve(coeffArr, 0, len(coeffArr)-1, rhs))
print(solvedp(coeffArr, rhs))
