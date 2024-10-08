# Plus Minus Permutation
def getPlusMinusPermutation(n, x, y):
    if x > y:
        x, y = y, x  # Swap x and y if x > y

    score = 0

    if x == y:
        # When x equals y, the score will always be 0.
        score = 0
    else:
        # Calculate the sum of values for all positions divisible by x.
        score += (n // x) * x * (n // x + 1) // 2

        # Calculate the sum of values for all positions divisible by y.
        score -= (n // y) * y * (n // y + 1) // 2


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print(getPlusMinusPermutation(n, x, y))
