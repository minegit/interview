def findAns(arr, lenA, temp, totalSum, ans, index):
    if totalSum == 0:
        ans.append(list(temp))
        return 
    for idx in range(index, lenA):
        if (totalSum - arr[idx]) >= 0:
            temp.append(arr[idx])
            findAns(arr, lenA, temp, totalSum-arr[idx], ans, idx)
            temp.remove(arr[idx])
    

    


def cSum(arr, totalSum):
    temp = []
    ans = []
    arr = sorted(list(set(arr)))
    index = 0
    lenA = len(arr)
    findAns(arr, lenA, temp, totalSum, ans, index)
    return ans


ans = cSum([2,4,6,8], 10)
print(ans)