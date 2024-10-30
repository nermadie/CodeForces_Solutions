# C. Left and Right Houses
import math


def solve(n, a):
    left_check_list = [True] + [False] * n
    count_0 = 0
    for i in range(1, n + 1):
        if a[i - 1] == "0":
            count_0 += 1
        if count_0 * 2 >= i:
            left_check_list[i] = True
    right_check_list = [False] * n + [True]
    count_1 = 0
    for i in range(n - 1, -1, -1):
        if a[i] == "1":
            count_1 += 1
        if count_1 * 2 >= n - i:
            right_check_list[i] = True

    left = math.floor(n / 2)
    right = math.ceil(n / 2)
    for i in range((n // 2) + 2):
        if left - i >= 0:
            if left_check_list[left - i] and right_check_list[left - i]:
                return left - i
        if right + i <= n:
            if left_check_list[right + i] and right_check_list[right + i]:
                return right + i
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    print(solve(n, a))
