# B1. The Strict Teacher (Easy Version)
def solve(n, m, q, b, a):
    b.sort()
    if b[0] > a[0]:
        return b[0] - 1
    if b[-1] < a[0]:
        return n - b[-1]
    for i in range(m - 1):
        if b[i] <= a[0] <= b[i + 1]:
            return (b[i + 1] - b[i]) // 2


t = int(input())
for _ in range(t):
    n, m, q = map(int, input().split())
    b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(solve(n, m, q, b, a))
