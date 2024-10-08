# Yarik and Array
def max_alternating_sum(n, a):
    if n == 1:
        return a[0]
    sum = a[0]
    ans = a[0]
    mn = min(0, a[0])
    for i in range(1, n):
        if abs(a[i] % 2) == abs(a[i - 1] % 2):
            mn = 0
            sum = 0
        sum += a[i]
        ans = max(ans, sum - mn)
        mn = min(mn, sum)
    return ans


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_alternating_sum(n, a))
