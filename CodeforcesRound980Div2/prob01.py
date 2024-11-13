# A. Profitable Interest Rate
import math


def solve(a, b):
    result = 0
    if a >= b:
        return a
    if 2 * a >= b:
        result = a - (b - a)
    return result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))
