# C. MEX rose
def solve(n, k, a):
  cnt_k = 0
  check_arr = [0] * (n+1)
  for i in range(n):
    check_arr[a[i]] += 1
    if a[i] == k:
      cnt_k += 1

  result_cnt = 0
  for i in range(k):
    if check_arr[i] == 0:
      result_cnt += 1

  return max(cnt_k, result_cnt)

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))

  print(solve(n, k, a))