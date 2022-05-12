class Node():
    def __init__(self, petrol, distance) -> None:
        self.petrol = petrol
        self.distance= distance
    def __repr__(self) -> str:
        return f"p:{self.petrol} d:{self.distance}"
def solve(A):
    remainingPetrol = 0
    initialNode = None
    initialCount = 0
    while True:
        currentPoint = A.pop(0)
        if initialNode == currentPoint:
            return initialNode
        if currentPoint.distance > (currentPoint.petrol + remainingPetrol):
            if currentPoint.petrol > currentPoint.distance:
                initialNode = currentPoint
                remainingPetrol = currentPoint.distance- currentPoint.petrol
            else:
                initialNode = None
                remainingPetrol = 0
            A.append(currentPoint)
            initialCount+=1
            if initialCount >= len(A):
                return -1
        else:
            remainingPetrol += currentPoint.petrol-currentPoint.distance
            A.append(currentPoint)
            if initialNode is None:
                initialNode = currentPoint
def solveOpt(A):
    start = 0
    capacity = 0
    deficit = 0
    n = len(A)
    for x in range(n):
        capacity += A[x].petrol-A[x].distance
        if capacity < 0:
            start = x +1
            deficit += capacity
            capacity = 0
    if capacity+deficit < 0:
        return -1
    return start
A = [(4,6), (6,5),(7,3),(4,5)]
A = [Node(5,6),Node(7,6),Node(2,3)]
print(solveOpt(A))