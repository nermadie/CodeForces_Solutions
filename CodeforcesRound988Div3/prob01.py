# A. Twice
def solve(n, a):
    a.sort()
    i = 0
    result = 0
    while i < n - 1:
        if a[i] == a[i + 1]:
            result += 1
            i += 2
        else:
            i += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
