# A. Split the Multiset
def solve(n, k):
    if n == 1:
        return 0
    if (n - 1) % (k - 1) == 0:
        return (n - 1) // (k - 1)
    else:
        return ((n - 1) // (k - 1)) + 1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
