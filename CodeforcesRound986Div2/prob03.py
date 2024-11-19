# C. Alice's Adventures in Cutting Cake
def solve(n, m, v, a):
    dp_left = [-1] * (m + 1)
    dp_right = [-1] * (m + 1)
    dp_left[0] = 0
    dp_right[0] = n
    suma_list = [0] * (n + 1)
    cur_sum_left = 0
    cur_sum_right = 0
    index_left = 1
    index_right = 1
    for i in range(n):
        suma_list[i + 1] = suma_list[i] + a[i]
        if index_left < m + 1:
            cur_sum_left += a[i]
            if cur_sum_left >= v:
                dp_left[index_left] = i + 1
                cur_sum_left = 0
                index_left += 1
        if index_right < m + 1:
            cur_sum_right += a[n - i - 1]
            if cur_sum_right >= v:
                dp_right[index_right] = n - i - 1
                cur_sum_right = 0
                index_right += 1
    result = -1
    for i in range(m + 1):
        if dp_left[i] == -1 or dp_right[m - i] == -1:
            continue
        result = max(result, suma_list[dp_right[m - i]] - suma_list[dp_left[i]])
    return result


t = int(input())
for _ in range(t):
    n, m, v = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, v, a))
