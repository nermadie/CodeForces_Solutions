# A. Minimal Coprime
def solve(l, r):
    return r - l + (1 if l == r == 1 else 0)


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(solve(l, r))
