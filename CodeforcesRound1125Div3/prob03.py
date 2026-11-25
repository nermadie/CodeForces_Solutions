# C. Unrequited Love
def solve(n, a):
    dict_result = {}
    ans = 0

    for i in range(n - 4):
        result = a[i] + a[i + 2] - a[i + 4]
        count = dict_result.get(result, 0)
        ans += count
        dict_result[result] = count + 1

    for i in range(n - 6):
        cur = a[i] + a[i + 2] - a[i + 4]
        if i + 2 < n - 4:
            temp = a[i + 2] + a[i + 4] - a[i + 6]
            if cur == temp:
                ans -= 1
        if i + 4 < n - 4:
            temp = a[i + 4] + a[i + 6] - a[i + 8]
            if cur == temp:
                ans -= 1

    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
