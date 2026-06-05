# C. Grid L
def get_divisors(n):
    divisors = []

    i = 3
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)

            if i * i != n:
                divisors.append(n // i)

        i += 1

    return divisors


def solve(n, m):
    N = n + m * 2
    alpha = 2 * N + 1
    divisors = get_divisors(alpha)
    for divisor in divisors:
        x = (divisor - 1) // 2
        y = ((alpha // divisor) - 1) // 2
        diff = abs(x - y)
        if diff <= n:
            return f"{x} {y}"
    return -1


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
