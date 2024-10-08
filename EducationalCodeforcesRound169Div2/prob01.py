# A. Closest Point
def solve(n, x):
    if n == 2 and abs(x[0] - x[1]) > 1:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    print(solve(n, x))
