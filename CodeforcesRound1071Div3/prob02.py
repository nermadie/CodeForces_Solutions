def solve(n, a):
    cur_max = abs(a[1] - a[0])
    for i in range(1, n - 1):
        cur_max = max(
            cur_max,
            abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i]) - abs(a[i + 1] - a[i - 1]),
        )
    cur_max = max(cur_max, abs(a[n - 1] - a[n - 2]))
    return sum(abs(a[i] - a[i - 1]) for i in range(1, n)) - cur_max


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
