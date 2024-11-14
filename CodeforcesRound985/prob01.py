# A. Set
def solve(l, r, k):
    return r // k - l + 1 if r // k >= l else 0


t = int(input())
for _ in range(t):
    l, r, k = map(int, input().split())
    print(solve(l, r, k))
