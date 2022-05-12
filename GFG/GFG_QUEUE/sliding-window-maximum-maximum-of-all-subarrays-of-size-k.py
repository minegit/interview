def maxValue(arr, N):
    if len(arr) <= N:
        return max(arr)
    Q = []
    maxVal = arr[0]
    for y in range(N):
        if maxVal < arr[y]:
            maxVal = arr[y]    
        Q.append(arr[y])
    print(maxVal, end=" ")
    for x in range(N, len(arr)):
        poppedVal = Q.pop(0)
        if poppedVal == maxVal:
            Q.append(arr[x])
            maxVal = max(Q)
        elif arr[x] > maxVal:
                maxVal = arr[x]
                Q.append(arr[x])
        else:
            Q.append(arr[x])
        print(maxVal, end=" ")

def findSlidingMax(arr, N):
    Q = []
    for x in range(0,len(arr)):
        if len(Q) > 0 and abs(x-Q[0]) == N:
            Q.pop(0)
        while len(Q) > 0 and arr[Q[-1]] < arr[x]:
            Q.pop(-1)
        Q.append(x)
        if x >= N-1:
            print(arr[Q[0]], end=" ")
        
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
# maxValue(arr, 4)

findSlidingMax(arr, 3)

