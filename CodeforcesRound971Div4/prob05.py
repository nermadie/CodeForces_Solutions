# E. Klee's SUPER DUPER LARGE Array!!!
# --------------------
def solve(n, start):
    sum_total = (2 * start + n - 1) * n // 2
    # sum_sub = i * start + ((i - 1) * i) // 2
    # value = 2 sum_sub - sum_total
    a = 1
    b = 2 * start - 1
    c = -(2 * start + n - 1) * n // 2

    delta = b**2 - 4 * a * c
    i1 = int((-b + delta**0.5) // (2 * a))
    result = min(
        abs(2 * (i1 * start + ((i1 - 1) * i1) // 2) - sum_total),
        abs(2 * ((i1 + 1) * start + (i1 * (i1 + 1)) // 2) - sum_total),
    )

    return result


t = int(input())
for _ in range(t):
    n, start = map(int, input().split())
    print(solve(n, start))
