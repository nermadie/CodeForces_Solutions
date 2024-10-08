# Chips on the Board
def solve_test_case(n, a, b):
    sum_row = sum(a)
    sum_col = sum(b)
    min_row = min(a)
    min_col = min(b)
    return (
        sum_row + min_col * n
        if sum_row + min_col * n < sum_col + min_row * n
        else sum_col + min_row * n
    )


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve_test_case(n, a, b))
