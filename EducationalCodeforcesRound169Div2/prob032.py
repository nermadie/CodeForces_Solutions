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
            print("DIFF: ", diff, "K: ", k)
            break
        else:
            k = k - diff
            if k == 0:
                break
    if init == 1:
        result += a[0]
    print(a)
    return result


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if i == 42:
        print(n, k)
        print(a)
        print(solve(n, k, a))
print(
    """4
13
0
0"""
)
