# D. Destruction of the Dandelion Fields
def solve(n, a):
  result = 0
  odd_list = []
  for i in range(n):
    if a[i] % 2 != 0:
      odd_list.append(a[i])
    else:
      result += a[i]
  if len(odd_list) == 0:
    return 0
  odd_list.sort()
  for i in range(len(odd_list)//2, len(odd_list)):
    result += odd_list[i]
  return result

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))