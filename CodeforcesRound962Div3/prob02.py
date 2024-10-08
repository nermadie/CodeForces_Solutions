# B. Scale
def solve(n, k, grid):
    for i in range(0, n, k):
        for j in range(0, n, k):
            print(grid[i][j], end="")
        print()


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    solve(n, k, grid)
