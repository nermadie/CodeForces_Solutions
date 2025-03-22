# A. Draw a Square
def solve(l, r, d, u):
    if l == r == d == u:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    print(solve(l, r, d, u))
