def heapify(A, i, lenA):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < lenA and A[left]>A[largest]:
        largest = left
    if right < lenA and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, lenA)
    
def solve(A):
    lenA = len(A)
    for x in range((lenA-2)//2, -1, -1):
        heapify(A, x, lenA)
    print(A)

arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
solve(arr)

