# C. Pacer
def solve(n, m, a, b):
  result = 0
  for i in range(n):
      if b[i] != b[i+1]:
        a_delta = a[i+1] - a[i]
        if a_delta % 2 == 0:
          result += a_delta - 1
        else:
          result += a_delta
      else:
        a_delta = a[i+1] - a[i]
        if a_delta % 2 == 0:
          result += a_delta
        else:
          result += a_delta - 1
  result += (m - a[n])
  return result

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  a = [0]
  b = [0]
  for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
  print(solve(n, m ,a, b))