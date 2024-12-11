# D. Attribute Checks
def solve(n, m, r):
    dp = [0] * (m + 5)
    curr = 0
    for val in r:
        if val == 0:
            curr += 1
            for i in range(m, -1, -1):
                if dp[i] < 0:
                    dp[i + 1] += dp[i]
                    dp[i] = 0
        elif abs(val) > curr:
            continue
        elif val > 0:
            dp[val] += 1
        else:
            dp[0] += 1
            dp[curr + val + 1] -= 1
    for i in range(m + 1):
        dp[i] += dp[i - 1]
    return max(dp)


n, m = map(int, input().split())
r = list(map(int, input().split()))
print(solve(n, m, r))
