# Raspberries
from traceback import print_tb


def solve(n, k, a):
    if k == 4:
        if n == 1:
            return 4 - (a[0] % 4)
        count2 = 0
        count3 = 0
        for item in a:
            remainder = item % 4
            if remainder == 0:
                return 0
            elif remainder == 2:
                count2 += 1
                if count2 == 2:
                    return 0
            elif remainder == 3:
                count3 = 1
        if count3 == 1 or count2 == 1:
            return 1
        return 2

    else:
        product = 1
        max_remainder = 0

        for i in range(n):
            if a[i] % k == 0:
                return 0
            else:
                max_remainder = max(max_remainder, a[i] % k)

        return k - max_remainder


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(n, k, a))
