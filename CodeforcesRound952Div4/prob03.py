# C. Good Prefixes
def solve(n, a):
    max_val = 0
    total = 0
    result = 0
    for i in range(n):
        total += a[i]
        if a[i] > max_val:
            max_val = a[i]
        if total - max_val == max_val:
            result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
