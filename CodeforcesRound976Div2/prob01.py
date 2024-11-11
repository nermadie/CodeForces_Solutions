# A. Find Minimum Operations
import math


def solve(n, k):
    if k == 1:
        return n
    result = 0
    while n != 0:
        result += n % k
        n = n // k
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
