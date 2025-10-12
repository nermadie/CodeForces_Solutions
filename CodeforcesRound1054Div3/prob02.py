# B. Unconventional Pairs
def solve(n, a):
  a.sort()
  max_diff = 0
  for i in range(0, n, 2):
    diff = a[i+1] - a[i]
    max_diff = max(diff, max_diff)
  return max_diff

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  print(solve(n, a))