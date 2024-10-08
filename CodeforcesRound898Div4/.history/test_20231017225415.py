def countWays(coins, S):
    n = len(coins)
    # Tạo một mảng dp với các giá trị ban đầu là 0.
    dp = [0] * (S + 1)
    # Có một cách để có tổng khối lượng là 0, không chọn đồng xu nào.
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], S + 1):
            dp[j] += dp[j - coins[i]]

    return dp[S]


# Ví dụ
coins = [1, 2, 3]
S = 4
ways = countWays(coins, S)
print("Số cách chọn đồng xu để có tổng khối lượng", S, "là:", ways)
