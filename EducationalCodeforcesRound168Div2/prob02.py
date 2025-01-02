# B. Make Three Regions
def solve(n, grid):
    result = 0
    for i in range(n - 2):
        if (
            grid[0][i] == "x"
            and grid[1][i] == "."
            and grid[0][i + 1] == "."
            and grid[1][i + 1] == "."
            and grid[0][i + 2] == "x"
            and grid[1][i + 2] == "."
        ) or (
            grid[0][i] == "."
            and grid[1][i] == "x"
            and grid[0][i + 1] == "."
            and grid[1][i + 1] == "."
            and grid[0][i + 2] == "."
            and grid[1][i + 2] == "x"
        ):
            result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(2):
        grid.append(input())
    print(solve(n, grid))
