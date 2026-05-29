def solve(n, k, s):
  num1 = s.count('1')
  num0 = n - num1
  count = num1 // 2 + num0 // 2
  mincount = abs(num1 - num0) // 2
  if count >= k and (count + k) % 2 == 0 and mincount <= k:
    return 'YES'
  return 'NO'

t = int(input())
for i in range(t):
  n, k = map(int, input().split())
  s = input()
  print(solve(n, k, s))