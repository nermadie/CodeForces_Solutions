# D. Yet Another Array Problem
def solve(n, a):
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
  for prime in primes:
    for i in range(n):
      if a[i] % prime != 0:
        return prime
  return -1

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))