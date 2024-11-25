for s in [*open(0)][1:]:
    n = int(s)
    print(
        *[
            a := [3 + i // 2 for i in range(n)],
            [1, *a[:8], 1, *a[8:21], 2, 2, 1, *a[21:-5]],
            [-1],
        ][n % 2 * 2 - (n > 26 and n & 1)]
    )
