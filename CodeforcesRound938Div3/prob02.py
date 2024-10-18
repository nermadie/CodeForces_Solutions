# B. Progressive Square
def solve(n, c, d, b):
    b.sort()
    a11 = b[0]
    a = []
    for i in range(n):
        for j in range(n):
            a.append(a11 + c * i + d * j)
    a.sort()
    for i in range(n * n):
        if a[i] != b[i]:
            return "no"
    return "yes"


t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    print(solve(n, c, d, b))
