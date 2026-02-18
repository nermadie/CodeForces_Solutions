# A. Letter Home
def solve(n, s, x):
    if n == 1:
        return abs(s - x[0])
    if s > x[0] and s > x[-1]:
        return s - x[0]
    if s < x[0] and s < x[-1]:
        return x[-1] - s
    return min(abs(s - x[0]), abs(s - x[-1])) * 2 + max(abs(s - x[0]), abs(s - x[-1]))


t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    print(solve(n, s, x))
