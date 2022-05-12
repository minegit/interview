def solve(S, m , N):
    if N == 0:
        return 1
    if N < 0:
        return 0
    if m <= 0 and N >0:
        return 0
    return solve(S, m-1, N) + solve(S, m, N-S[m-1])


def solveDp(S, numberOfCoins, totalSum):
    dp =  [[ 0 for x in range(numberOfCoins)] for y in range(totalSum+1)]
    for x in range(numberOfCoins):
        dp[0][x] = 1 # ways of getting change with X coins for 0 total sum. 
    
    for amount in range(1, totalSum+1):
        for coin in range(numberOfCoins):
            # Count of soln with reduced amount and same coin
            includingCoin = dp[amount-S[coin]][coin] if amount - S[coin] >= 0 else 0
             # Count of soln with same amount but reduced coin.
            excludingCoin = dp[amount][coin -1] if coin >= 1 else 0
            dp[amount][coin] = includingCoin + excludingCoin
        # print(dp)
    return dp[amount][coin]
    
    

S = [1,2,3]
m = len(S)
import time

N = 400
t = time.process_time()
x = solve(S, m, N)
elapsed_time = time.process_time() - t
print(elapsed_time)
print(x)
