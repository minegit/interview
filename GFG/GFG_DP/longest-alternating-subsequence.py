def solve(arr):
    increment, decrement = 1, 1
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            increment  = decrement+1
        elif arr[i] < arr[i-1]:
            decrement = increment +1

    return max(increment, decrement)

a = [10, 22, 9, 33, 49, 50, 31, 60]
print(solve(a))