# B. Farmer John's Card Game
def solve(n, m, grid):
  for i in range(n):
    grid[i].sort()

  indexed = list(enumerate(grid))
  indexed.sort(key=lambda x: x[1][0])
  cur = 0
  for j in range(m):
    for i in range(n):
      if indexed[i][1][j] != cur:
        print(-1)
        return
      cur += 1
  for i in range(n):
    print(indexed[i][0] + 1, end=" ")
  print()


t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  grid = [list(map(int, input().split())) for _ in range(n)]
  solve(n, m, grid)