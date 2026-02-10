# D. Monster Game
def _init_lr(arr, l, r):
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1
    return l, r


def bs_asc_last_le(arr, x, l=None, r=None):
    l, r = _init_lr(arr, l, r)
    res = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] <= x:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res


def solve(n, a, b):
    dict_a = {}
    for i in range(n):
        dict_a.setdefault(a[i], 0)
        dict_a[a[i]] += 1
    list_a = sorted(dict_a.items(), key=lambda x: x[0])

    sword_needs = [0] * (n + 1)
    for i in range(n):
        sword_needs[i + 1] = sword_needs[i] + b[i]

    max_lv_can_obtain = -1
    # for i in range(n, -1, -1):
    #     if sword_needs[i] <= n:
    #         max_lv_can_obtain = i
    #         break
    max_lv_can_obtain = bs_asc_last_le(sword_needs, n)

    result = max_lv_can_obtain
    sword_left = n

    for diff, minus_sword in list_a:
        result = max(result, diff * max_lv_can_obtain)
        sword_left -= minus_sword
        # for i in range(max_lv_can_obtain, -1, -1):
        #     if sword_needs[i] <= sword_left:
        #         max_lv_can_obtain = i
        #         break
        max_lv_can_obtain = bs_asc_last_le(
            sword_needs, sword_left, 0, max_lv_can_obtain
        )

    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
