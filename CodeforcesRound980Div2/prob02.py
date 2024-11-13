# B. Buying Lemonade
def solve(n, k, a):
    a.sort()
    result = 0
    for i in range(n):
        if (n - i) * (a[i] - (a[i - 1] if i > 0 else 0)) < k:
            result += (n - i) * (a[i] - (a[i - 1] if i > 0 else 0)) + 1
            k -= (n - i) * (a[i] - (a[i - 1] if i > 0 else 0))
        else:
            result += k
            break
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
