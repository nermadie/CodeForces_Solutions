# C. Can I Square?
import math


def can_build_square(squares):
    total = 0
    for item in squares:
        total += item
    if math.sqrt(total).is_integer():
        return "YES"
    else:
        return "NO"


t = int(input())

for _ in range(t):
    n = int(input())
    squares = list(map(int, input().split()))
    print(can_build_square(squares))
