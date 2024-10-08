# A. Only Pluses
def solve(a, b, c):
    a, b, c = sorted([a, b, c])
    for i in range(5):
        a += 1
        a, b, c = sorted([a, b, c])
    return a * b * c


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
