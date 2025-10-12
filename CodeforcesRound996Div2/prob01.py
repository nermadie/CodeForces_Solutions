# A. Two Frogs
def solve(n, a, b):
    diff = abs(a - b)
    if diff % 2 == 0:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print(solve(n, a, b))
