# E. Reverse the Rivers
# https://medium.com/analytics-vidhya/bisect-module-in-python-6b78f8c37beb
from bisect import bisect_left, bisect_right


def solve(n, k, transpose, m, queries):

    top = 0
    bottom = n - 1
    for query in queries:
        region, sign, value = query.split()
        region = int(region) - 1
        value = int(value)
        if sign == ">":
            top = max(
                top, bisect_left(transpose[region], value + 1, lo=top, hi=bottom + 1)
            )
        else:
            bottom = min(
                bottom,
                bisect_right(transpose[region], value - 1, lo=top, hi=bottom + 1) - 1,
            )
    return top + 1 if top <= bottom else -1


n, k, q = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(k):
        grid[i][j] |= grid[i - 1][j]
transpose = [[grid[j][i] for j in range(n)] for i in range(k)]
for _ in range(q):
    m = int(input())
    queries = []
    for _ in range(m):
        queries.append(input())
    print(solve(n, k, transpose, m, queries))
