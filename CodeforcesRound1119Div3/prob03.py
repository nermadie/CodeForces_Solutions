def solve(n, a):
    for i in range(n):
        if a[i] == 1:
            break
        if a[i] == -1:
            a[i] = 1
            break
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            break
        if a[i] == -1:
            a[i] = 1
            break

    for i in range(n):
        if a[i] == -1:
            a[i] = 0

    print(" ".join(map(str, a)))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)
