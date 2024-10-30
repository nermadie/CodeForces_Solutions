# B. Fireworks
def solve(a, b, m):
    return (m // a) + (m // b) + 2


t = int(input())
for _ in range(t):
    a, b, m = map(int, input().split())
    print(solve(a, b, m))
