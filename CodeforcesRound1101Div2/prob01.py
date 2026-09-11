def solve(n, a):
    a.sort()
    set_a = set(a)
    count_set_a = len(set_a)
    check_list = [(0, 0)] * (count_set_a)
    prev_count = 0
    cur_count = 1
    check_list_index = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cur_count += 1
        else:
            check_list[check_list_index] = (prev_count, n - cur_count - prev_count)
            prev_count += cur_count
            cur_count = 1
            check_list_index += 1
    check_list[check_list_index] = (prev_count, n - cur_count - prev_count)
    result = 99999999
    for i in range(count_set_a):
        result = min(max(check_list[i][0], check_list[i][1]), result)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
