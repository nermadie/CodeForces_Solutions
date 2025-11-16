# A. Fibonacciness
def solve(a1, a2, a4, a5):
  result = 0
  for a3 in range(-100, 101):
    cnt = 0
    if a1 + a2 == a3:
      cnt += 1
    if a2 + a3 == a4:
      cnt += 1
    if a3 + a4 == a5:
      cnt += 1
    result = max(result, cnt)
    if result == 3:
      return result
  return result


t = int(input())
for _ in range(t):
  a1, a2, a4, a5 = map(int, input().split())
  print(solve(a1, a2, a4, a5))