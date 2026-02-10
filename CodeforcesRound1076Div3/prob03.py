# C. Replace and Sum
def solve(n, q, a, b, lr):
    a[-1] = max(a[-1], b[-1])
    for i in range(n - 2, -1, -1):
        a[i] = max(a[i], a[i + 1], b[i])
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    result = []
    for l, r in lr:
        result.append(prefix_sum[r] - prefix_sum[l - 1])
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    lr = [list(map(int, input().split())) for _ in range(q)]
    print(solve(n, q, a, b, lr))
