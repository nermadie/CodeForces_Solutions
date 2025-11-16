# C. Isamatdin and His Magic Wand!
def solve(n, a):
  odd_exist = False
  even_exist = False

  for i in range(n):
    if a[i] % 2 == 0:
      even_exist = True
    else:
      odd_exist = True
  if even_exist and odd_exist:
    a.sort()
  return " ".join(map(str, a))

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))