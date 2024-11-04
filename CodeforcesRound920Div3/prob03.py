# C. Sending Messages
def solve(n, f, a, b, m):
    for i in range(n):
        cur_min_unit = float("inf")
        if i == 0:
            cur_min_unit = min(a * m[i], b)
        else:
            cur_min_unit = min(a * (m[i] - m[i - 1]), b)
        f -= cur_min_unit
        if f <= 0:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n, f, a, b = map(int, input().split())
    m = list(map(int, input().split()))
    print(solve(n, f, a, b, m))
