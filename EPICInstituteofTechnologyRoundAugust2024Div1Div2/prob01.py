# A. Distanced Coloring
def solve(n, m, k):
    return min(n, k) * min(m, k)


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
