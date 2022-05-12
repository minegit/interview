import heapq
def minOperations(a,n):
        data = []
        res = 0
        for i in range(n):
            if data and data[0] < a[i]:
                res += a[i] - data[0]
                heapq.heappush(data,a[i])
                heapq.heappop(data)
                continue
            heapq.heappush(data,a[i])
        return res

print(minOperations([2,5,1,2,1], 5))
