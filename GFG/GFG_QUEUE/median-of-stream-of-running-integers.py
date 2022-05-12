from heapq import heappop, heappush

## Maintain Min heap of numbers greater that median and max heap of numbers smaller than median
# root position of both the heap will be near to  centre of sorted of array
# if both heap is os same lengtht then current number will make the arr as ODD so one 
# element will me median if heapsizes are different then avg of roots of heaps will be the median

def solve(arr):
    if len(arr) == 1:
        return arr[0]
    med = arr[0]
    print(med, end=" ")
    minheap = []
    maxheap = []
    heappush(minheap, med)
    for x in range(1, len(arr)):
        print("procrssing for index :",x, "Value", arr[x])
        if len(minheap) > len(maxheap):
            if arr[x] < med:
                heappush(maxheap, -1*arr[x])
            else:
                poppedMinValue = heappop(minheap)
                heappush(minheap, arr[x])
                heappush(maxheap, -1*poppedMinValue)
            med = (minheap[0] + -1*maxheap[0])/2
        elif len(minheap) < len(maxheap):
            if arr[x] < med:
                poppedMaxValue = -1 * heappop(maxheap)
                heappush(minheap, poppedMaxValue)
                heappush(maxheap, -1 * arr[x])
            else:
                heappush(minheap, arr[x])
            med = (minheap[0] + -1*maxheap[0])/2
        else:
            if arr[x] < med:
                heappush(maxheap, -1*arr[x])
                med = maxheap[0] * -1
            else:
                heappush(minheap, arr[x])
                med = minheap[0]
        print(med, end=" ")
solve([5, 15, 10, 20, 3,1,100,25])
