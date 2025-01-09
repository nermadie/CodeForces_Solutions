# A. Coin Transformation
def solve(n):
    i = 0
    while 4**i <= n:
        i += 1
    return 2 ** (i - 1)


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
