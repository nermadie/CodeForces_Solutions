# C. Mad MAD Sum
def solve(n, a):
    result = 0
    time = 2
    cur_a = None
    while time:
        result += sum(a)
        dict_a_count = {}
        cur_a = []
        cur_mad_key = 0
        for item in a:
            dict_a_count.setdefault(item, 0)
            dict_a_count[item] += 1
            if dict_a_count[item] >= 2 and item > cur_mad_key:
                cur_mad_key = item
            cur_a.append(cur_mad_key)
        time -= 1
        a = cur_a
    cur_sum = 0
    for i in range(2, n):
        cur_sum += cur_a[i]
        result += cur_sum
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
