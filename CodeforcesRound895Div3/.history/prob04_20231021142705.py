# Plus Minus Permutation
def getPlusMinusPermutation(n, x, y):
    divisible_by_x = n // x
    divisible_by_y = n // y
    divisible_by_x_y = n // (x * y)
    total_x = divisible_by_x - divisible_by_x_y
    total_y = divisible_by_y - divisible_by_x_y
    sumx = ((2 * n - total_x + 1) * total_x) // 2
    sumy = ((1 + total_y) * total_y) // 2
    print(sumx, sumy)
    return sumx - sumy


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print(getPlusMinusPermutation(n, x, y))
