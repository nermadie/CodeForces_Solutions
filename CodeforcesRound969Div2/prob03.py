# C. Dora and C++
# ax + by = k(gcd(a, b)) with k>=1
import math


def solve(n, a, b, c):
    if a != b:
        a = math.gcd(a, b)
    c = [item % a for item in c]
    c.sort()
    min_val = c[n - 1] - c[0]
    for i in range(n):
        min_val = min(min_val, c[i - 1] + a - c[i])
    return min_val


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    print(solve(n, a, b, c))
