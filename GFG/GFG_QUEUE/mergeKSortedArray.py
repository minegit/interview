import sys
def compareArr(Arr):    
    while True:
        minValue = sys.maxsize
        minArray = None
        for x in range(0, len(Arr)):
            if len(Arr[x]) != 0:
                if minValue > Arr[x][0]:
                    minValue = Arr[x][0]
                    minArray = x
        if minArray is None:
            break
        Arr[minArray].pop(0)
        print(minValue, end=" ")


arr = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]

arr = [[], [2, 4, 10, 12,20,22], [3, 7, 9, 11,25],[0,13, 14, 15, 16]]
compareArr(arr)
