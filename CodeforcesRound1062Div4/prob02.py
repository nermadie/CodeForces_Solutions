# B. Your Name
def solve(n, s, t):
  chars = [0] * 26
  for i in range(n):
    chars[ord(s[i]) - 97] += 1
  for i in range(n):
    chars[ord(t[i]) - 97] -= 1
    if chars[ord(t[i]) - 97] < 0:
      return "NO"
  return "YES"

t = int(input())
for _ in range(t):
  n = int(input())
  s, t = input().split()
  print(solve(n, s, t))