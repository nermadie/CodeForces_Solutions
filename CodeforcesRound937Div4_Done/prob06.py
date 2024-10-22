# F. 0, 1, 2, Tree!
from math import ceil


def solve(a, b, c):
    edges_for_c = a + 1
    if c != edges_for_c:
        return -1
    empty_edges = 1
    a_remaining = a
    height = 0
    for i in range(18):
        if a_remaining > 2**i:
            a_remaining -= 2**i
        elif a_remaining > 0:
            height += i + 1
            empty_edges = 2**i - a_remaining
            break
        else:
            break

    if empty_edges > 0 and a != 0:
        b -= empty_edges
    height += ceil(b / (a_remaining * 2 + empty_edges))
    return height


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
