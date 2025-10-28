# A. New World, New Me, New Array
def solve(n, k, p):
  k = abs(k)
  p = abs(p)
  if k == 0:
    return 0
  if p * n < k:
    return -1
  result = 1
  for i in range(n):
    if result* p < k:
      result += 1
    else:
      return result
t = int(input())
for _ in range(t):
  n, k, p = map(int, input().split())
  print(solve(n, k, p))