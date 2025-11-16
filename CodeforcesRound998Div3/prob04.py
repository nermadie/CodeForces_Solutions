# D. Subtract Min Sort
def solve(n, a):
  for i in range(n-1):
    if a[i+1] < a[i]:
      return "NO"
    a[i+1] -= a[i]
  return "YES"

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))