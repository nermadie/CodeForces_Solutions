# C. New Game
from collections import Counter


def solve(n, k, a):
    a.sort()
    c = Counter(a)
    a_list = list(c.items())
    max_count = a_list[0][1]
    cur_count = a_list[0][1]
    cur_len = 1
    for i in range(len(a_list) - 1):
        if a_list[i + 1][0] > a_list[i][0] + 1:
            cur_count = a_list[i + 1][1]
            cur_len = 1
        else:
            cur_count += a_list[i + 1][1]
            cur_len += 1
            if cur_len > k:
                cur_count -= a_list[i - k + 1][1]
                cur_len -= 1
        max_count = max(max_count, cur_count)
    return max_count


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
