# D. Come a Little Closer
def solve(n, xy):
  pass

t = int(input())
for _ in range(t):
  n = int(input())
  xy = [tuple(map(int, input().split())) for _ in range(n)]
  print(solve(n, xy))