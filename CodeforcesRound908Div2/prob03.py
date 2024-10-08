# Anonymous Informant
def can_obtain_array_b(n, k, b):
    if n == 1:
        return "Yes" if b[0] == 1 else "No"
    set_b = set()
    even_n = n % 2 == 0
    check_symmetric = even_n
    for i in range(n):
        if b[i] <= n:
            set_b.add(b[i])
        if even_n and i < n // 2 and b[i] != b[n // 2 + i]:
            check_symmetric = False

    queue = []
    for item in set_b:
        # from_index, shift_left, cur_operation, appeared_status
        queue.append((0, item, 1, {(0, item): 1}))
    while queue:
        print(queue)
        from_index, shift_left, cur_operation, appeared_status = queue.pop(0)
        real_index = from_index - shift_left
        if -real_index >= n:
            real_index += n
        if b[shift_left - 1 + real_index] == shift_left:
            if cur_operation == k:
                return "Yes"
            else:
                for item in set_b:
                    if (real_index, item) not in appeared_status:
                        new_appear_status = dict(appeared_status)
                        new_appear_status[(real_index, item)] = cur_operation + 1
                        queue.append(
                            (real_index, item, cur_operation + 1, new_appear_status)
                        )
                    else:
                        prev_operation = appeared_status[(real_index, item)]
                        if (k - prev_operation + 1) % (
                            cur_operation + 1 - prev_operation
                        ) == 0:
                            return "Yes"
    return "No"


# Input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    result = can_obtain_array_b(n, k, b)
    print(result)
