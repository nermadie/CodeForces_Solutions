# C1. Cirno and Number (Easy Version)
def get_diff(a, b):
    return abs(int(a) - int(b))


def solve(a_string, n, d1, d2, is_first_time=True):
    a = int(a_string)
    first_digit = int(a_string[0])

    if first_digit > d2:
        smaller = str(d2) * n
        if is_first_time:
            if d1 == 1:
                larger = str(d1) * (n + 1)
                return min(get_diff(a, smaller), get_diff(a, larger))
            elif d2 == 1:
                larger = "1" + str(d1) * n
                return min(get_diff(a, smaller), get_diff(a, larger))
        return get_diff(a, smaller)

    if first_digit < d1:
        larger = str(d1) * n
        if is_first_time and n > 1:
            smaller = str(d2) * (n - 1)
            return min(get_diff(a, smaller), get_diff(a, larger))
        else:
            return get_diff(a, larger)

    if d1 < first_digit < d2:
        smaller = str(d2) + str(d1) * (n - 1)
        larger = str(d1) + str(d2) * (n - 1)
        return min(get_diff(a, smaller), get_diff(a, larger))

    if n == 1:
        return 0

    if first_digit == d1:
        larger = str(d2) + str(d1) * (n - 1)
        smaller_diff = solve(a_string[1:], n - 1, d1, d2, False)
        if is_first_time:
            temp = str(d2) * (n - 1)
            smaller_diff = min(smaller_diff, get_diff(a, temp))
        return min(get_diff(a, larger), smaller_diff)
    if first_digit == d2:
        smaller = str(d1) + str(d2) * (n - 1)
        larger_diff = solve(a_string[1:], n - 1, d1, d2, False)
        if is_first_time:
            temp = str(d1) * (n - 1)
            larger_diff = min(larger_diff, get_diff(a, temp))
        return min(get_diff(a, smaller), larger_diff)


t = int(input())
for i in range(t):
    a, n = map(int, input().split())
    d1, d2 = map(int, input().split())
    a_string = str(a)
    print(solve(a_string, len(a_string), d1, d2))
#     if i == 4516:
#         print(a, n, d1, d2)

# print("""0
# 0
# 111
# 2556""")
