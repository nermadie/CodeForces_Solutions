# A. Blocked
def solve(n, a):
    a.sort(reverse=True)
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            return -1
    return " ".join(map(str, a))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
