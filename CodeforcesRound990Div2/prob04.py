# D. Move Back at a Cost
def solve(n, a):

    sorted_a = sorted(enumerate(a), key=lambda x: x[1])
    move_list = []
    result = []

    prev_index = -1
    for i in range(n):
        index, value = sorted_a[i]
        if index > prev_index:
            result.append(value)
            prev_index = index
        else:
            move_list.append(value + 1)

    if len(result) == n:
        return " ".join(map(str, result))
    move_list.sort()
    # find the first ele that > than move_list[0] in result using binary search
    l, r = 0, len(result) - 1
    while l < r:
        mid = (l + r) // 2
        if result[mid] <= move_list[0]:
            l = mid + 1
        else:
            r = mid
    if result[r] > move_list[0]:
        move_list.extend(map(lambda i: i + 1, result[r:]))
        move_list.sort()
        result = result[:r]
    result.extend(move_list)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
