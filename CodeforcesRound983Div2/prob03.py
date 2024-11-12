# C. Trinity
def solve(n, a):
    a.sort()
    result = 0
    for i in range(2, n):
        if a[result] + a[result + 1] <= a[i]:
            result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
