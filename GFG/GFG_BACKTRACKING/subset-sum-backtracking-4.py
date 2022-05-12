def isSubSetSum(currIdx, N,A, totalSum, subsetSum,solnSet):
    if totalSum == subsetSum:
        return True
    if currIdx >= N:
        return False
    for idx in range(currIdx, N):
        elem = A[idx]
        if subsetSum+elem <= totalSum:
            subsetSum+=elem
            solnSet.append(elem)
            if isSubSetSum(idx+1, N, A, totalSum, subsetSum,solnSet):
                print(solnSet)
            subsetSum-=elem
            solnSet.remove(elem)
    
def solve(A, totalSum):
    subsetSum = 0
    currIdx = -1
    N = len(A)
    solnSet = []
    x = isSubSetSum(currIdx+1, N, A, totalSum, subsetSum,solnSet)
    print(x)
if __name__ == "__main__":
    A = [2,4,6,8]
    A = [15, 22, 14, 26, 32, 9, 16, 8]
    solve(A, 53)