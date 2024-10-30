# A. Setting up Camp
import math


def solve(a, b, c):
    if b % 3 != 0 and (b % 3) + c < 3:
        return -1
    rooms_bc = 0 if b % 3 == 0 else 1
    c_remaining = c - (3 - (b % 3)) if b % 3 != 0 else c
    rooms_c = math.ceil(c_remaining / 3)
    return a + b // 3 + rooms_bc + rooms_c


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
