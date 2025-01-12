# C. Hungry Games
def solve(n, x, a):
    ans = 0
    t = 0
    c = n * (n + 1) // 2
    for i in range(n - 1, -1, -1):
        t += a[i]
        if t > x:
            ans += i + 1
            t = 0
    print(c - ans)


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, x, a)
