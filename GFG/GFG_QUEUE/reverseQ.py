def reverse(Q):
    if len(Q) == 0:
        return 
    item = Q.pop(0)
    reverse(Q)
    Q.append(item)

def findMinIndex(Q, uptoIndex, N):
    minVal = 9999
    minIndex = -1
    for i in range(N) :
        curr = Q.pop(0)
        if curr  <= minVal and i < uptoIndex:
            minVal = curr
            minIndex = i
        Q.append(curr)
    return minIndex

def sendMinValueToRear(Q, minIndex,N):
    for x in range(0, N):
        curr = Q.pop(0)
        if x != minIndex:
            Q.append(curr)
        else:
            minValue = curr
    Q.append(minValue)

def sort(Q, N):
    for x in range(N, 0, -1):
        minIndex = findMinIndex(Q,x, N)
        sendMinValueToRear(Q, minIndex , N)
    print(Q)  

Q = [11,5,4,21]
sort(Q, len(Q))
# print(Q)