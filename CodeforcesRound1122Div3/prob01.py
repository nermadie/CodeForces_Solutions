# A. Good Contest
def solve(n, a1, a2, a3):
    return n - min(a1, a2, a3)


t = int(input())
for _ in range(t):
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    print(solve(n, a1, a2, a3))
