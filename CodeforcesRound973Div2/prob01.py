# A. Zhan's Blender
def solve(n, x, y):
    min_time = min(x, y)
    result = n / min_time
    if result.is_integer():
        return int(result)
    else:
        return int(result) + 1


t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    print(solve(n, x, y))
