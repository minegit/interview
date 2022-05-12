def solve(A, startIndex, endIndex):
    if startIndex == endIndex :
        return 0
    if A[startIndex] == 0:
        return float('inf')
    minJump = float('inf')
    for i in range(startIndex+1, endIndex+1):
        if i < startIndex+A[startIndex]+1:
            jumps = solve(A, i, endIndex)
            if jumps != float('inf') and jumps +1 < minJump:
                minJump = jumps+1
    
    return minJump

arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
n = len(arr)
print('Minimum number of jumps to reach',
     'end is', solve(arr, 0, n-1))