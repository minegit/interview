from collections import defaultdict
def solve1(A, K):
    numberFreqMap = defaultdict(int)
    for x in A:
        numberFreqMap[x]+=1
    v= []
    temp = 0
    for number, freq in numberFreqMap.items():
        v.append(freq)
        temp+=(freq-1)
    if K<= temp:
        return len(v)
    K = K- temp
    ans = len(v)
    return ans -K

print(solve1([1,2,2,2], 1))
