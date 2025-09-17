# B. Lasers
def solve(n, m, x, y, a, b):
    return n + m

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, x, y, a, b))