# C. The Legend of Freya the Frog
# ------------------------------
def solve(x, y, k):
    x_direction = x // k + 1 if x % k != 0 else x // k
    y_direction = y // k + 1 if y % k != 0 else y // k

    return (x_direction * 2) - 1 if x_direction > y_direction else y_direction * 2


t = int(input())  # Number of test cases
for _ in range(t):
    x, y, k = map(int, input().split())
    print(solve(x, y, k))
