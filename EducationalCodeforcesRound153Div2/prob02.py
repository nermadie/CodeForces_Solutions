# Fancy Coins
def solve(m, k, a1, ak):
    max_k_coins = m // k
    least_m_coins = m % k
    if ak >= max_k_coins:
        return least_m_coins - a1 if least_m_coins > a1 else 0
    else:
        diff_k = max_k_coins - ak
        if least_m_coins > a1:
            return least_m_coins - a1 + diff_k
        else:
            remaining_m_to_k = (a1 - least_m_coins) // k
            return diff_k - remaining_m_to_k if diff_k > remaining_m_to_k else 0


t = int(input())

for _ in range(t):
    m, k, a1, ak = map(int, input().split())

    print(solve(m, k, a1, ak))
