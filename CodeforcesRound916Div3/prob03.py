# C. Quests
def solve(n, k, a, b):
    result = 0
    max_b_kpre_list = [0] * n
    max_b_kpre_list[0] = b[0]
    for i in range(1, n):
        max_b_kpre_list[i] = max(b[i], max_b_kpre_list[i - 1])
    result = 0
    sum_a = 0
    for i in range(k if k < n else n):
        sum_a += a[i]
        result = max(result, sum_a + max_b_kpre_list[i] * (k - i - 1))
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, k, a, b))
