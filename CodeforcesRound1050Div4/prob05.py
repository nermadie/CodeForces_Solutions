# E. Split
def solve(n, k, a):
  arr = [0] * (n+1)
  for i in range(n):
    arr[a[i]] += 1
  ref_arr = [0] * (n+1)
  for i in range(n):
    if arr[i] != 0 and arr[i] % k != 0:
        return 0
    else:
        ref_arr[i] = arr[i] // k
  result = 0
  for i in range(n):
    temp_arr = [0] * (n+1)
    for j in range(i, n):
      temp_arr[a[j]] += 1
    check = True
    for j in range(n):
      if temp_arr[j] > ref_arr[j]:
        check = False
        break
    if check:
      result += 1
  return result


t = int(input())
for _ in range(t):
  n, k  = map(int, input().split())
  a = list(map(int, input().split()))
  print(solve(n, k, a))