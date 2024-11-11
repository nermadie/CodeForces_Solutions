# B. Brightness Begins
import math


def solve(k):
    if k < 3:
        return k + 1
    if k < 7:
        return k + 2
    count = int((-1 + math.isqrt(1 + 4 * k)) / 2)
    cur_n = ((4 + count * 2) * count) // 2
    remain = 0
    if k > cur_n - count:
        remain = k - (cur_n - count - 1)
    return cur_n + remain


# n = 3 + 5 + 7 + 9 + 11 + ...
# k >= n - count
# k >= (3 + 1 + count * 2) * count / 2 - count
# k >= (4 + count * 2) * count / 2 - count
# k >= count + count^2
# count^2 + count - k <= 0
# count = (-1 + sqrt(1 + 4k)) / 2

t = int(input())
for _ in range(t):
    k = int(input())
    print(solve(k))
