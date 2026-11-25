# B. Stakes and Shapes
def solve(x, y, z):
    n = x + y + z
    arr = [x, y, z]
    arr.sort()
    if z == arr[-1]:
        return "S" * n
    elif y == arr[-1]:
        return "R" * n
    else:
        return "P" * n


t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    print(solve(x, y, z))
