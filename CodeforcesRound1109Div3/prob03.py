def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, x, y, p):
    g = gcd(x, y)
    for i in range(n):
        if abs(p[i] - i - 1) % g != 0:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, x, y, p))
