# C. Game of Mathletes
def solve(n, k, x):
  num_list = [0] * (n + 1)
  for num in x:
    num_list[num] += 1

  result = 0
  odd_temp = 0
  if k % 2 == 0:
    result += num_list[k//2] // 2
  else:
    odd_temp = 1
  for i in range(1, (k // 2) + odd_temp):
    if i * 2 == k:
      continue
    if k - i > 0 and k - i <= n:
      result += min(num_list[i], num_list[k - i])
  return result

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  x = list(map(int, input().split()))
  print(solve(n, k, x))