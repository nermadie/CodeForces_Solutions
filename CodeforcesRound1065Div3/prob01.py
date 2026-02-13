# A. Shizuku Hoshikawa and Farm Legs
def solve(n):
    if n % 2 != 0:
        return 0
    return n // 4 + 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
