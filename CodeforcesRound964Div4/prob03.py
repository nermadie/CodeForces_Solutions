# C. Showering
def solve(n, s, m, lr):
    prev_r = 0
    for item in lr:
        if item[0] - prev_r >= s:
            return "YES"
        prev_r = item[1]
    if m - prev_r >= s:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    n, s, m = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, s, m, lr))
