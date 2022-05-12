from heapq import heapify, heappop, heappush

def solve(inputArr):
    if len(inputArr) == 2:
        return inputArr[0]+inputArr[1]
    temp  = []
    for x in inputArr:
        heappush(temp, x)
    additionSum = 0
    while len(temp)>2:
        firstElem = heappop(temp)
        secondElem = heappop(temp)
        additionSum += (firstElem+secondElem)
        heappush(temp, firstElem+secondElem)
    return additionSum+firstElem+secondElem

print(solve([6,4,3,2]))

    