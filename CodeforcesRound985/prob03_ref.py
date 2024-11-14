for _ in range(int(input())):
    n = int(input())

    def f(a, x):
        return a + (a < x) - (a > x)

    dp = [0, -n, -n]
    for x in map(int, input().split()):
        dp[2] = max(f(dp[1], x), f(dp[2], x))
        dp[1] = max(dp[1], dp[0])
        dp[0] = f(dp[0], x)

    print(max(dp[1], dp[2]))
