# C. Hungry Games
def solve(n, x, a):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    dp = [0] * (n + 2)
    right_boundary = n + 1
    for i in range(n, 0, -1):
        left = i
        right = right_boundary
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[mid] - prefix_sum[i - 1] > x:
                right = mid
            else:
                left = mid + 1
        right_boundary = left
        dp[i] = dp[left + 1] + (left - i) if left <= n else left - i
    return sum(dp)


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, x, a))
