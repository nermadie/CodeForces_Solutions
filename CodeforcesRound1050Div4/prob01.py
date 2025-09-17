# A. Sublime Sequence
def solve(x, n):
    if n % 2 == 0:
      return 0
    return x

t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    print(solve(x, n))
