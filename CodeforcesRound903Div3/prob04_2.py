# Divide and Equalize
import math


def is_possible_to_equalize(n, arr):
    total = 1
    for i in range(n):
        total *= arr[i]
    i = 1
    temp_total = round(math.pow(i, n))
    while temp_total <= total:
        if total == temp_total:
            return "YES"
        else:
            i += 1
            temp_total = round(math.pow(i, n))
    return "NO"


# Input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = is_possible_to_equalize(n, arr)
    print(result)
