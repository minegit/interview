def solveRecur(arr_sorted, partitionSum, includedEle, maxPartitionSum, K, lenArr,partitionIndex, limitIndex):
    if partitionSum[partitionIndex] == maxPartitionSum:
        if(partitionIndex == K-2):
            return True
        return solveRecur(arr_sorted, partitionSum, includedEle, maxPartitionSum,K, lenArr, partitionIndex+1, lenArr-1)
    for x in range(limitIndex, -1 ,-1):
        if(includedEle[x]):
            continue
        tmp = partitionSum[partitionIndex]+arr_sorted[x]
        if tmp<= maxPartitionSum:
            includedEle[x] = True
            partitionSum[partitionIndex] = tmp
            nxt = solveRecur(arr_sorted, partitionSum, includedEle, maxPartitionSum, K, lenArr,partitionIndex, x-1)
            includedEle[x] = False
            partitionSum[partitionIndex] -= arr_sorted[x]
            if nxt:
                return True
    return False
def solve(arr, K):
    if K == 1:
        return arr
    lenArr = len(arr)
    if K > lenArr:
        return -1
    arr_sum = sum(arr)
    if arr_sum % K != 0:
        return -1
    partitionSum = [0]*K
    maxPartitionSum = arr_sum//K
    for i in range(lenArr):
        if arr[i] > maxPartitionSum:
            return -1
    arr_sorted = sorted(arr)
    includedEle = [False] * lenArr
    partitionSum[0] = arr_sorted[-1]
    includedEle[lenArr-1] = True
    partitionIndex = 0
    limitIndex = lenArr-1
    return solveRecur(arr_sorted, partitionSum, includedEle, maxPartitionSum, K, lenArr,partitionIndex, limitIndex );

arr = [2, 1, 4, 5, 3, 3 ]
d = solve(arr, 3)
print(d)
