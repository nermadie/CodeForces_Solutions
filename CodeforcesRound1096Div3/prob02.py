# B. Party Monster
def solve(n, s):
  if n % 2 == 1:
    return "NO"
  if s.count("(") != s.count(")"):
    return "NO"
  return "YES"

t = int(input())
for _ in range(t):
  n = int(input())
  s = input()
  print(solve(n, s))