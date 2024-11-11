# E. Rudolf and k Bridges
def solve(n, m, k, d, a):
    pass


t = int(input())
for _ in range(t):
    n, m, k, d = map(int, input().split())
    a = []
    for _ in range(m):
        a.append(list(map(int, input().split())))
    print(solve(n, m, k, d, a))
