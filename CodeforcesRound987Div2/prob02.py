# B. Penchick and Satay Sticks
def solve(n, p):
    for i in range(n):
        if abs(p[i] - (i + 1)) > 1:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
