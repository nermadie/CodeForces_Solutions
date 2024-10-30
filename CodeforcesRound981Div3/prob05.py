# E. Sakurako, Kosuke, and the Permutation
import math


def solve(n, p):
    result = 0
    mem = [0] * (n)
    for i in range(n):
        cur_pos = i
        if mem[i] == 1:
            continue
        mem[i] = 1
        count = 1
        while mem[p[cur_pos] - 1] == 0:
            mem[p[cur_pos] - 1] = 1
            cur_pos = p[cur_pos] - 1
            count += 1
        result += math.ceil(count / 2) - 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
