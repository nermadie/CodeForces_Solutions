# C. Longest Good Array
def solve(l, r):
    diff = r - l
    # (n+1) * n / 2 -> n^2/2 + n/2
    # n^2/2 + n/2 = diff
    # n^2 + n = 2 * diff
    # n^2 + n - 2 * diff = 0
    # n = (-1 + sqrt(1 + 8 * diff)) / 2
    n = (-1 + (1 + 8 * diff) ** 0.5) / 2
    # if n.is_integer():
    #     return int(n)
    # else:
    return int(n) + 1


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(solve(l, r))
