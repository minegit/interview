from heapq import heapify, heappop, heappush


def sortK(arr, n, k):
    heap = arr[:k+1]
    heapify(heap)
    target_index = 0
    for remaining_index in range(k+1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[remaining_index])
        target_index+=1
    while heap:
        arr[target_index] = heappop(heap)
        target_index+=1

def sortX(arr, n, k):
    
    while n != k:
        temp = []
        for x in range(0, n, 2):
            if x == n-1:
                temp.append(arr[x])   
            else: 
                temp.append(min(arr[x], arr[x+1]))
        arr = temp
        n = len(arr)
    print(arr)



arr = [2, 6, 3, 12, 56, 8]
arr = [3, 6, 100, 9, 10, 12, 7, -1, 10,0]
n = len(arr)
sortX(arr, n, 3)
# print(arr)