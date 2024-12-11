# C. Alya and Permutation
def solve(n):
    if n % 2 == 1:
        print(n)
        print(" ".join(map(str, (list(range(2, n - 1)) + [1, n - 1, n]))))
    else:
        exp = 1
        while 2**exp <= n:
            exp += 1
        print(2**exp - 1)
        exp -= 1
        pre_last_val = 2**exp - 1
        print(
            " ".join(
                map(
                    str,
                    list(range(2, pre_last_val - 1))
                    + list(range(pre_last_val + 1, n))
                    + [1, pre_last_val - 1, pre_last_val]
                    + [n],
                )
            )
        )


t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
