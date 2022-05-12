def solve(A, m, S):
    if S == 0:
        return True
    if S > 0 and m == 0:
        return False
    if A[m-1] > S:
        return solve(A, m-1, S)
    return solve(A, m-1, S) or solve(A, m-1, S-A[m-1])


def solveDp(A, m, S):
    dp = [[False for x in range(S+1)] for y in range(m+1)]
    for x in range(m+1):
        dp[x][0] = True
    for y in range(1, S+1):
        dp[0][y] = False
    for elem in range(1, m+1):
        for amount in range(1, S+1):
            if amount < A[elem-1]:
                dp[elem][amount] = dp[elem-1][amount]
            else:
                dp[elem][amount]  = dp[elem-1][amount] or dp[elem-1][amount-A[elem-1]]

    return dp[m][S]

def solveDpBetterSpace(A, m, S):
    dp = [[False for x in range(S+1)] for y in range(3)]
    for elem in range(m+1):
        for amount in range(S+1):
            if amount == 0:
                dp[elem%2][amount] = True
            elif elem == 0:
                dp[0][amount] = False
            elif amount >= A[elem-1]:
                dp[elem %2][amount] = dp[(elem+1)%2][amount] or dp[(elem+1)%2][amount-A[elem-1]]
            else:
                dp[elem %2][amount] = dp[(elem+1)%2][amount]
    return dp[m%2][S]

def solveDpSingleArray(A, m, S):
    dp = [False] * (S+1)
    dp[0]= True # sum of 0 is always possible
    for elem in A:
        for amount in range(S, elem -1, -1):
            if dp[amount - elem]:
                dp[amount] = True
    return dp[S]


set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)

x = solveDpSingleArray(set, n, sum)
print(x)