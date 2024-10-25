# E. Vlad and an Odd Ordering
def solve(n, k):
    cur_count = 0
    if n % 2 == 0:
        cur_count = n // 2
    else:
        cur_count = n // 2 + 1
    if k <= cur_count:
        return 2 * k - 1
    exp_2 = 0
    prev_count = 0
    while k > cur_count:
        exp_2 += 1
        prev_count = cur_count
        all_divisors = n // (1 << exp_2)
        if all_divisors % 2 == 0:
            cur_count += all_divisors // 2
        else:
            cur_count += all_divisors // 2 + 1
    return ((k - prev_count) * 2 - 1) * (1 << exp_2)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
