# C. Huge Pile
import math


def solve(n, k):
    if n < k:
        return -1
    temp_set = {n}
    count = 0
    while True:
        if k in temp_set:
            return count
        new_set = set()
        for num in temp_set:
            if num == 1:
                continue
            new_set.add(math.ceil(num / 2))
            new_set.add(math.floor(num / 2))
        if len(new_set) == 0:
            return -1
        temp_set = new_set
        count += 1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
