# Vasilije in Cacak
def is_possible(n, k, x):
    sum_last_k_num = (n + (n - k + 1)) * k // 2
    sum_first_k_num = (1 + k) * k // 2
    if sum_last_k_num >= x >= sum_first_k_num:
        return "YES"
    else:
        return "NO"


# Input
t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    print(is_possible(n, k, x))
