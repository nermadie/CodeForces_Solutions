# C. Light Switches
def solve(n, k, a):
    max_a = max(a)
    set_a_remain = set()
    for item in a:
        n_times = (max_a - item) // k
        if n_times % 2 == 1:
            n_times += 1
        set_a_remain.add(n_times * k + item - max_a)
    max_set_a_remain = max(set_a_remain)
    min_set_a_remain = min(set_a_remain)
    if max_set_a_remain - min_set_a_remain >= k:
        return -1
    return max_a + max_set_a_remain


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
