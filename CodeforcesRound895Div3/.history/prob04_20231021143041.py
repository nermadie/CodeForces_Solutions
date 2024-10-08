# Plus Minus Permutation
def getGCD(x, y):
    if x == 0:
        return y
    return getGCD(y % x, x)


def getLCM(x, y):
    return (x * y) // getGCD(x, y)


def getPlusMinusPermutation(n, x, y):
    divisible_by_x = n // x
    divisible_by_y = n // y
    divisible_by_x_y = n // getLCM(x, y)
    total_x = divisible_by_x - divisible_by_x_y
    total_y = divisible_by_y - divisible_by_x_y
    sumx = ((2 * n - total_x + 1) * total_x) // 2
    sumy = ((1 + total_y) * total_y) // 2
    return sumx - sumy


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print(getPlusMinusPermutation(n, x, y))
