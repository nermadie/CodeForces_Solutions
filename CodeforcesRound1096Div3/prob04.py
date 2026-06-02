# D. Palindromex
def solve(n, a):
    first_0_index = -1
    last_0_index = -1
    for i in range(2 * n):
        if first_0_index == -1:
            if a[i] == 0:
                first_0_index = i
        else:
            if a[i] == 0:
                last_0_index = i

    result = 1
    # start with center is 0 and expand to left and right, case 1st 0
    check_list = [0] * (n + 1)
    check_list[0] = 1
    for i in range(1, n):
        if first_0_index - i >= 0 and first_0_index + i < 2 * n:
            if a[first_0_index - i] != a[first_0_index + i]:
                break
            check_list[a[first_0_index - i]] = 1
        else:
            break
    for i in range(n + 1):
        if check_list[i] == 0:
            result = max(result, i)
            break

    # start with center is 0 and expand to left and right, case 2nd 0
    check_list = [0] * (n + 1)
    check_list[0] = 1
    for i in range(1, n):
        if last_0_index - i >= 0 and last_0_index + i < 2 * n:
            if a[last_0_index - i] != a[last_0_index + i]:
                break
            check_list[a[last_0_index - i]] = 1
        else:
            break
    for i in range(n + 1):
        if check_list[i] == 0:
            result = max(result, i)
            break

    # the palindrome contain both 0
    check_list = [0] * (n + 1)
    check_list[0] = 1
    # inner check
    scope = (last_0_index - first_0_index) // 2
    for i in range(1, scope + 1):
        if a[first_0_index + i] != a[last_0_index - i]:
            return result
        check_list[a[first_0_index + i]] = 1
    # outer check
    for i in range(1, n):
        if first_0_index - i >= 0 and last_0_index + i < 2 * n:
            if a[first_0_index - i] != a[last_0_index + i]:
                break
            check_list[a[first_0_index - i]] = 1
        else:
            break
    for i in range(n + 1):
        if check_list[i] == 0:
            result = max(result, i)
            break
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
