# B. The Third Side
def solve(n, a):
    return sum(a) - len(a) + 1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
