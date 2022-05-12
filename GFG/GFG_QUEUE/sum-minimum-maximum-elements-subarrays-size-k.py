def solve(A, k):
    Q =[]
    minMaxSum = 0
    minElement = A[0]
    maxElement = A[0]
    for x in range(k):
        Q.append(A[x])
        if minElement > A[x]:
            minElement = A[x]
        if maxElement < A[x]:
            maxElement = A[x]
    minMaxSum = minElement+maxElement
    for x in range(k, len(A)):
        popped  = Q.pop(0)
        if popped == minElement:
            minElement = min(Q)
        if popped == maxElement:
            maxElement = max(Q)
        if A[x]< minElement:
            minElement = A[x]
        if A[x] > maxElement:
            maxElement = A[x]
        Q.append(A[x])
        minMaxSum += (minElement+maxElement)
    print(minMaxSum)

solve([2, 5, -1, 7, -3, -1, -2], 4)       
    