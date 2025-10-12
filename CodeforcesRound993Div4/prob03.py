# C. Hard Problem
def solve(m, a, b, c):
    remain = max(m - a, 0) + max(m - b, 0)
    return min(a, m) + min(b, m) + min(c, remain)


t = int(input())
for _ in range(t):
    m, a, b, c = map(int, input().split())
    print(solve(m, a, b, c))
