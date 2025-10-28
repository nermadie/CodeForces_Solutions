# B. Beautiful String
def solve(n, s):
  print(s.count("0"))
  result = []
  for i in range(n):
     if s[i] == '0':
        result.append(i)
  return ' '.join(str(x + 1) for x in result)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(solve(n, s))