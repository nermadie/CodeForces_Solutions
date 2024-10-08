def minCoins(coins, K):
    n = len(coins)
    result = 0

    for i in range(n - 1, -1, -1):
        while K >= coins[i]:
            K -= coins[i]
            result += 1

    return result


# Ví dụ
coins = [1, 3, 6, 10]
K = 12
min_coins = minCoins(coins, K)
print("Số tờ tiền ít nhất để có được", K, "đồng là:", min_coins)
