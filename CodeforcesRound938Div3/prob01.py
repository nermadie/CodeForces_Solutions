# A. Yogurt Sale
def solve(n, a, b):
    if 2 * a > b:
        return (n // 2) * b + (n % 2) * a
    else:
        return n * a


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print(solve(n, a, b))
