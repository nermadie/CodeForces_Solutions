# A. Square?
def solve(a,b,c,d):
  return "YES" if a==b and b==c and c==d else "NO"

t = int(input())
for _ in range(t):
  a,b,c,d = map(int, input().split())
  print(solve(a,b,c,d))
