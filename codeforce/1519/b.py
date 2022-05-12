# N = int(input())
# for x in range(N):
#     x, y, K = list(map(int, input().split()))
#     myK = x*y-1 # x*(y-1)+x-1
#     if K == myK:
#         print("YES")
#     else:
#         print("NO")

# 1462-B
# def solve(s, l):
#     if l == 4 and s == "2020":
#         return "YES"
#     len_t = l-4
#     for x in range(5):
#         lhs = s[0:x]
#         rhs=s[x+len_t:l]
#         if lhs+rhs == "2020":
#             return "YES"
#     return "NO"
# # s1 = "20192020"
# # solve(s1, len(s1))
# for x in range(int(input())):
#     l = int(input())
#     s = input()
#     print(solve(s,l))


# def solve(x):
#     if x > 45:
#         return -1
#     if x <=9 :
#         return x
#     arr = []
#     for i in range(9, 0, -1):
#         if x > 9:
#             arr.append(str(i))
#             x=x-i
#         elif x <= 9:
#             if str(x) not in arr:
#                 arr.append(str(x))
#                 break
#             else:
#                 x = x-i
#                 arr.append(str(i))
#     arr.sort()
#     return "".join(arr)
# # print(solve(15))
# for _ in range(int(input())):
#     x = int(input())
#     print(solve(x))

def solve(arr):
    s1 = set()
    y = 0
    for x in arr:
        if x in s1:
            x= x+1
        s1.add(x)
    return len(s1)

# arr = [1,1,3,4,5]
# solve(arr)

def solve1(n):
    if n ==1:
        return 1
    if n == 2:
        return 5
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for x in range(2, (n+1)):
        dp[x] = 4*(x-1)+dp[x-1]
    return dp[x]
print(solve1(int(input())))
# for _ in range(int(input())):
#     l = int(input())
#     x = list(map(int, input().split()))
#     print(solve(x))

