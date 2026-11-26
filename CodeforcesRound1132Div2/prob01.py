# A1. 15K4JR3B (Easy Version)
def solve(n):
    return (n // 2) * (n - (n // 2))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
