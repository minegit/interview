def solve(n):
    if n ==1 :
        return 1
    n2 = n3 = n5 = 0
    ans = [0] *(n+1)
    ans[0] = 1
    next2 = ans[n2] * 2
    next3 = ans[n3] * 3
    next5 = ans[n5] * 5
    for i in range(1, n):
        ans[i] = min(next2, next3, next5)
        print(i+1, "--->", ans[i])
        if ans[i] == next2:
            n2+=1
            next2  = ans[n2] * 2
        if ans[i] == next3:
            n3+=1
            next3  = ans[n3] * 3
        if ans[i] == next5:
            n5+=1
            next5  = ans[n5] * 5
    return ans

solve(150)

