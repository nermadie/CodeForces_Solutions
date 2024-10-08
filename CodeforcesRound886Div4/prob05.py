# Cardboard for Pictures
def find_w(n, c, sizes):
    square_sizes = 0
    sum_sizes = 0
    for item in sizes:
        square_sizes += item * item
        sum_sizes += item
    # 4 * i^2 + 4 * sum_sizes * i + square_sizes - c = 0
    return int(
        (-(4 * sum_sizes) + ((4 * sum_sizes) ** 2 - 16 * n * (square_sizes - c)) ** 0.5)
        / (8 * n)
    )


t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    sizes = list(map(int, input().split()))

    result = find_w(n, c, sizes)
    print(result)
