from re import S


def solveMax(A):
    currentMax = A[0]
    maxSofar = A[0]
    for x in A[1:]:
        currentMax = max(x, currentMax+x)
        maxSofar = max(maxSofar, currentMax)
    return maxSofar
def solveMin(A):
    currentMax = A[0]
    maxSofar = A[0]
    for x in A[1:]:
        currentMax = min(x, currentMax+x)
        maxSofar = min(maxSofar, currentMax)
    return maxSofar

def solve(A):
    lenA  = len(A)
    maxEndingHere = 0
    currentMax = -1 * 10000
    s = 0
    end = 0
    for i in range(lenA):
        maxEndingHere += A[i]
        if currentMax < maxEndingHere:
            currentMax = maxEndingHere
            start = s
            end = i
        if maxEndingHere < 0:
            maxEndingHere = 0
            s = i+1
    print(currentMax, s, end)

a = [-2, -3, 4, -1, -2, 1, 5, -3]
a1 = [3, -4, 2, -3, -1, 7, -5]
print(solveMin(a1))