def solve(N, diff):
    if abs(diff) > N:
        return 0
    if N ==1 and diff == 0:
        return 2
    if N == 1 and abs(diff) ==1:
        return 1
    return solve(N-1, diff) * 2 + solve(N-1, diff+1)+solve(N-1, diff-1)

x = solve(1, 1)
print(x)