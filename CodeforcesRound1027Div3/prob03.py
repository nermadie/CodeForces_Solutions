# C. Need More Arrays
def solve(n, a):
  cur  =a[0]
  result = 1
  for i in range(n):
    if a[i] > cur + 1:
      result += 1
      cur = a[i]
  return result


t = int(input())
for i in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))