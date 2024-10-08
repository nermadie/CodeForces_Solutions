# A. X Axis
def solve(x1, x2, x3):
    x1, x2, x3 = sorted([x1, x2, x3])
    return abs(x1 - x2) + abs(x2 - x3)


t = int(input())
for _ in range(t):
    x1, x2, x3 = map(int, input().split())
    print(solve(x1, x2, x3))
