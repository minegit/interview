def solve(stationTime, transferTime, entryTime, exitTime):
    stationCount=len(stationTime[0])
    t1 = [0] * stationCount
    t2 = [0] * stationCount
    t1[0] = entryTime[0]+stationTime[0][0]
    t2[0] = entryTime[1]+stationTime[0][0]

    for i in range(1, stationCount):
        t1[i] = min(t1[i-1]+stationTime[0][i], t2[i-1]+transferTime[1][i]+stationTime[0][i])
        t2[i] = min(t2[i-1]+stationTime[1][i], t1[i-1]+transferTime[0][i]+stationTime[1][i])
    min_time  = min(t1[stationCount-1]+exitTime[0], t2[stationCount-1]+exitTime[1])
    return min_time

a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
  
print(solve(a, t, e, x))