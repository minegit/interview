from heapq import heapify, heappush
from queue import PriorityQueue


def solve(A, K):
    minheap = []
    arr = []
    k = 0
    for x in A:
        if len(minheap) < K:
            heappush(minheap, x)
            arr.append(x)
            print(-1, end=" ")
        else:
            minValue = minheap[0]
            print(minValue, end=" ")
            minheap.remove(arr[0])
            heapify(minheap)
            arr.pop(0)
            heappush(minheap, x)
            arr.append(x)
A = [10, 20, 11, 70, 50, 40, 100, 5]
solve(A, 3)


