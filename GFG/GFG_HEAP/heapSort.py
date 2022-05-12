def heapify(arr, heapsize, root):
    parent = root
    left, right = 2*parent+1, 2*parent+2
    if left < heapsize and arr[parent] < arr[left]:
        parent = left
    if right < heapsize and arr[parent] < arr[right]:
        parent = right
    if parent != root:
        arr[parent], arr[root] = arr[root], arr[parent]
        heapify(arr, heapsize, parent)
def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")