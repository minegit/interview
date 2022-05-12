from re import X


def solve(A, N):
    if N == 0:
        return 0
    if N == 9 : 
        return 9
    A.sort()
    Q = A.copy()
    if 0 in A:
        Q.remove(0)
    count = 1
    while True:
        x= Q.pop(0)
        if int(x) % N == 0:
            if count == 50:
                return
            count+=1
            print(f"""{count} : {x}""")
        for y in A:
            Q.append(str(x)+str(y))
print(solve([1,8, 0,9], 23))
