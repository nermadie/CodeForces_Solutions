# A. Perpendicular Segments
# (x, y) (-y, x)
def solve(x, y, k):
    min_xy = min(x, y)
    return (min_xy, 0, 0, min_xy), (0, 0, min_xy, min_xy)


t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    a, b = solve(x, y, k)
    print(*a)
    print(*b)
