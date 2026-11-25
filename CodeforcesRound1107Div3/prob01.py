# A. Divide and Conquer
def solve(x, y):
    if x % y == 0:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(solve(x, y))
