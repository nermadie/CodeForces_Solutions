# C. Splitting Items
def solve(n, k, a):
    a.sort()
    result = 0
    init = 0
    if n % 2 == 1:
        init = 1
    for i in range(init, n - 1, 2):
        diff = a[i + 1] - a[i]
        if diff > k:
            result += diff - k
            k = 0
        else:
            k = k - diff
    if init == 1:
        result += a[0]
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
