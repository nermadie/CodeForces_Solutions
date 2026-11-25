def solve(n, a):
    cur = 0
    expected = 0
    for i in range(n):
        cur += a[i]
        expected += i + 1
        if cur < expected:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
