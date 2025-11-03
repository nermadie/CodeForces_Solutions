# B. Tournament
def solve(n, j, k, a):
  if k == 1:
    if min(a) != a[j - 1]:
      if max(a) != a[j - 1]:
        return "NO"
    else:
      for i in range(n):
        if a[i] != a[j - 1]:
          return "NO"
  return "YES"

t = int(input())
for _ in range(t):
  n, j, k = map(int, input().split())
  a = list(map(int, input().split()))
  print(solve(n, j, k, a))