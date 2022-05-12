def solve(lA, A):
    dp = 1
    maxLen = 1
    for i in range(1, lA):
        if A[i] > A[i-1]:
            dp = dp +1
            if maxLen < dp:
                maxLen = dp
        else:
            dp = 1
    print(maxLen)

# A=[1,7,2,11,15]
# solve(5, A)

lA = int(input())
A = list(map(int, input().split()))
solve(lA , A)