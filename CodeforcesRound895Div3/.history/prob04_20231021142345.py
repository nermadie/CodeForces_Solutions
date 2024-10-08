# Plus Minus Permutation
def getPlusMinusPermutation(n, x, y):
    divisible_by_x = n // x
    divisible_by_y = n // y
    divisible_by_x_y = n // (x * y)
    total_x = divisible_by_x - divisible_by_x_y
    total_y = divisible_by_y - divisible_by_x_y
    return ((1 + total_x) * total_x) // 2 + ((2 * n - total_y + 1) * total_y) // 2


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print(getPlusMinusPermutation(n, x, y))
