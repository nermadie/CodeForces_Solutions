# A. Legs
def solve(n):
    return n // 4 + n % 4 // 2


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
