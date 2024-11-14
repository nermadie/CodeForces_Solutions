# C. New Rating
def get_ratings(cur_ratings, contest_ratings):
    return (
        cur_ratings + (contest_ratings > cur_ratings) - (contest_ratings < cur_ratings)
    )


def solve(n, a):
    dp = [1, 0, 0]
    for i in range(1, n):
        dp[2] = max(get_ratings(dp[2], a[i]), get_ratings(dp[1], a[i]))
        dp[1] = max(dp[0], dp[1])
        dp[0] = get_ratings(dp[0], a[i])
    return max(dp[2], dp[1])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
