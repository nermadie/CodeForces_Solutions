# C. Prefix Min and Suffix Max
def solve(n, a):
  min_list = [0] * n
  max_list = [0] * n
  cur_min = 10**9 + 1
  cur_max = 0
  for i in range(n):
    if a[i] < cur_min:
      cur_min = a[i]
    min_list[i] = cur_min
  for i in range(n - 1, -1, -1):
    if a[i] > cur_max:
      cur_max = a[i]
    max_list[i] = cur_max

  result = []
  for i in range(n):
    if a[i] == min_list[i] or a[i] == max_list[i]:
      result.append("1")
    else:
      result.append("0")
  return "".join(result)


t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))