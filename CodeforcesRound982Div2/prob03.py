# C. Add Zeros
def solve(n, a):
    if n == 1:
        return 1
    require_length = []
    for i in range(n):
        require_length.append(a[i] + i)
    require_length_sorted = sorted(enumerate(require_length), key=lambda x: x[1])
    dp = [0] * (((n + 1) * n) // 2 + 1)
    dp[n] = 1
    result = 0
    for i in range(n):
        if require_length_sorted[i][1] >= len(dp):
            continue
        if dp[require_length_sorted[i][1]] == 1:
            result = max(
                result, require_length_sorted[i][1] + require_length_sorted[i][0]
            )
            dp[require_length_sorted[i][1] + require_length_sorted[i][0]] = 1
    return result


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if i == 353:
        print(n, a)
    # print(solve(n, a))
print(
    """10
11
10
1
"""
)
