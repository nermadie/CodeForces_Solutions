# A. Rectangle Arrangement
def solve(n, wh):
    max_w = 0
    max_h = 0
    for w, h in wh:
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return 2 * (max_w + max_h)


t = int(input())
for _ in range(t):
    n = int(input())
    wh = []
    for _ in range(n):
        wh.append(list(map(int, input().split())))
    print(solve(n, wh))
