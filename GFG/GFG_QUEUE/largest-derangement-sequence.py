from queue import PriorityQueue


def solveLargest(A):
    lenA = len(A)
    pq = PriorityQueue(maxsize=lenA)
    result = [0] * lenA
    for x in A:
        pq.put(-1 * x)
    for i in range(lenA):
        poppedValue = -1 * pq.get()
        if poppedValue != A[i] or i == lenA -1:
            result[i] = poppedValue
        else:
            result[i] = -1 * pq.get()
            pq.put(-1*poppedValue)
    if result[lenA-1] == A[lenA-1]:
        result[lenA-1], result[lenA-2] = result[lenA-2], result[lenA-1]
    print(result)
def solveSmallest(A):
    lenA = len(A)
    pq = PriorityQueue(maxsize=lenA)
    result = [0] * lenA
    for x in A:
        pq.put(x)
    for i in range(lenA):
        poppedValue = pq.get()
        if poppedValue != A[i] or i == lenA -1:
            result[i] = poppedValue
        else:
            result[i] = pq.get()
            pq.put(poppedValue)
    if result[lenA-1] == A[lenA-1]:
        result[lenA-1], result[lenA-2] = result[lenA-2], result[lenA-1]
    print(result)

seq = [ 92, 3, 52, 13, 2, 31, 1 ]
solveSmallest(seq)

