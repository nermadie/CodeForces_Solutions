# A. Alyona and a Square Jigsaw Puzzle
import math


def solve(n, a):
    cur_step = 1
    result = 1
    for i in range(1, n):
        cur_step += a[i]
        if math.sqrt(cur_step).is_integer() and int(math.sqrt(cur_step)) % 2 == 1:
            result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
