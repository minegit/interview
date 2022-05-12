import sys

def solve(coins, totalSum):
    dp = [0 for x in range(totalSum+1)]
    dp[0] = 0
    for amount in range(1,totalSum+1):
        minChangeCount = sys.maxsize-1
        for coin in coins:
            if amount-coin >=0:
                if minChangeCount > dp[amount-coin]:
                    minChangeCount = dp[amount-coin]
        dp[amount] = minChangeCount+1
    if dp[totalSum] == sys.maxsize:
        return -1
    
    return dp[totalSum]

print(solve([2,6], 11))
