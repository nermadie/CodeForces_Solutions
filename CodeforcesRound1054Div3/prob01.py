# A. Be Positive
def solve(n, a):
  pos = []
  nev = []
  zcnt = 0
  for i in range(n):
    if a[i] < 0:
      nev.append(a[i])
    elif a[i] == 0:
      zcnt += 1
    else:
      pos.append(a[i])
  result = zcnt
  nev.sort()
  if len(nev) % 2 != 0:
    result += 1 - nev[-1]
  return result
  
t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  print(solve(n, a))