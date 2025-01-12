# A. Diverse Game
def solve(n, m, grid):
    if n * m == 1:
        print(-1)
        return
    for i in range(n):
        for j in range(m):
            cur_val = grid[i][j] % (n * m) + 1
            print(cur_val, end=" ")
        print()


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    solve(n, m, grid)
