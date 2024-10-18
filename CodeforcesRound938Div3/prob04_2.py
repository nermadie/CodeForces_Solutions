from collections import Counter

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = input().split()
    b = input().split()
    cb = Counter(b)
    ca = Counter(a[:m])
    res = 0
    s = sum((ca & cb).values())
    if s >= k:
        res += 1
    for r in range(m, n):
        if ca[a[r]] < cb[a[r]]:
            s += 1
        ca[a[r]] += 1
        if ca[a[r - m]] <= cb[a[r - m]]:
            s -= 1
        ca[a[r - m]] -= 1
        if s >= k:
            res += 1
    print(res)
