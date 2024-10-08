# Money Trees
def find_max_length_subarray(arr, k):
    max_len = 0
    n = len(arr)
    result_arr = [k] * (n + 1)
    check = True
    while check:
        check = False
        temp_value = result_arr[max_len]
        for i in range(max_len + 1, n + 1):
            if temp_value is None:
                temp_value = result_arr[i]
                result_arr[i] = None
                continue
            fruit_left = temp_value - arr[i - 1]
            if fruit_left >= 0:
                temp_value = result_arr[i]
                result_arr[i] = fruit_left
                check = True
            else:
                temp_value = result_arr[i]
                result_arr[i] = None
        max_len += 1
    return max_len - 1


def max_subarray_length(n, k, a, h):
    # Handle h
    ok_subarr = []
    subarr = []
    for i in range(n - 1):
        if h[i] % h[i + 1] == 0:
            if len(subarr) <= 1:
                subarr.append(i)
            elif len(subarr) == 2:
                subarr[1] = i
        else:
            if len(subarr) == 1:
                subarr.append(i)
            elif len(subarr) == 2:
                subarr[1] = i
            ok_subarr.append(subarr)
            subarr = []
    if len(subarr) > 0:
        print(1)
        ok_subarr.append([subarr[0], n - 1])

    # Handle a
    max_len = 0
    print(ok_subarr)
    for item in ok_subarr:
        max_len = max(max_len, find_max_length_subarray(a[item[0] : item[1] + 1], k))
    return max_len


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    result = max_subarray_length(n, k, a, h)
    print(result)
