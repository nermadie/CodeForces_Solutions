# B. Rudolf and 121
def solve(n, a):
    for i in range(n - 2):
        a[i + 1] -= 2 * a[i]
        a[i + 2] -= a[i]
        if a[i + 1] < 0 or a[i + 2] < 0:
            return "NO"
    if a[-1] == 0 and a[-2] == 0:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
