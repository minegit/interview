from collections import Counter
def solve(A, N):
    charCountMap = Counter(A)
    charCountList = charCountMap.most_common()
    maxChar, maxCount = charCountMap.most_common()[0] 

    if maxCount > (N+1)//2 :
        return None
    res = [None] * N
    ind = 0

    while maxCount:
        res[ind] = maxChar
        ind+=2
        maxCount-=1
    charCountMap[maxChar] = 0
    
    for char, count in charCountMap.items():
        for y in range(count):
            if ind >= N:
                ind = 1
            res[ind] = char
            ind+=2
    print("".join(res))

A = "bbbaaasdfddsdfsasfdsasdffas"
solve(A, len(A))
