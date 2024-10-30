# D. Seraphim the Owl
def solve(n, m, a, b):
    dp = [0] * (n + 1)
    result = float("inf")
    for pos in range(n - 1, -1, -1):
        dp[pos] = dp[pos + 1] + min(a[pos], b[pos])
        if pos < m:
            result = min(result, dp[pos + 1] + a[pos])
    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, a, b))
