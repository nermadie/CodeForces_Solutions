# B. Prefix Max
def solve(n, a):
    return n * max(a)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
