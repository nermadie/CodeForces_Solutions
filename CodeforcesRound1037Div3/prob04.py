def solve(n, k, grid):
    grid.sort()
    result = k
    for i in range(n):
        if grid[i][0] <= result <= grid[i][1]:
            result = max(result, grid[i][2])

    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(n, k, grid))
