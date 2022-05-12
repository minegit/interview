def solve(S, lS):
    t = "QAQ"
    m = 3
    dp = [0] * (m+1)
    dp[0] = 1
    for c in range(0, lS):
        for x in range(m-1, 0, -1):
            print(c,"--->",S[c], x,"------>",t[x])
            if t[x] ==  S[c]:
                print(dp)
                dp[x+1] += dp[x]
                print(dp)
    
    print(dp)
    return dp[m]

S = "QAQAQ"
solve(S, len(S))