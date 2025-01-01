# A. Greedy Monocarp
def solve(n, k, a):
    a.sort(reverse=True)
    sum_a = sum(a)
    if sum_a < k:
        return k - sum_a
    for i in range(n):
        k -= a[i]
        if k < 0:
            return a[i] + k
        elif k == 0:
            return 0


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
