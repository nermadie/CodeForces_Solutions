# E. Money Buys Happiness
def solve(m, x, c, h):
    max_h = sum(h)
    dp = [None] * (max_h + 1)
    dp[0] = 0
    for i in range(m):
        for j in range(max_h, -1, -1):
            if dp[j] is not None:
                if dp[j] + c[i] <= i * x and j + h[i] <= max_h:
                    dp[j + h[i]] = (
                        min(dp[j + h[i]], dp[j] + c[i])
                        if dp[j + h[i]] is not None
                        else dp[j] + c[i]
                    )
    for i in range(max_h, -1, -1):
        if dp[i] is not None:
            return i


t = int(input())
for _ in range(t):
    m, x = map(int, input().split())
    c_list = []
    h_list = []
    for _ in range(m):
        c, h = map(int, input().split())
        c_list.append(c)
        h_list.append(h)
    print(solve(m, x, c_list, h_list))
