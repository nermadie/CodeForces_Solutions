# A. Koshary
def solve(x, y):
  if x % 2 == 1 and y % 2 == 1:
    return "NO"
  return "YES"

t= int(input())
for _ in range(t):
  x, y = map(int, input().split())
  print(solve(x,y))