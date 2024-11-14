# B. Kar Salesman
import math


def solve(n, x, a):
    a.sort()
    sum_a = sum(a)
    if sum_a <= x * a[-1]:
        return a[-1]
    else:
        sum_a -= a[-1] * x
        return math.ceil(sum_a / x) + a[-1]


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, x, a))
