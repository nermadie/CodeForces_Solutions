def solve(n, h):
    h.sort()
    if n == 1:
        return 1
    return h[-1] - h[0] + 1


t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(solve(n, h))
