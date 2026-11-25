import math


def solve(n, s):
    longest = 0
    cur = 0
    for i in range(n):
        if s[i] == "#":
            cur += 1
            longest = max(longest, cur)
        else:
            cur = 0

    return math.ceil(longest / 2)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
