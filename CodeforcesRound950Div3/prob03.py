# C. Sofia and the Lost Operations
def solve(n, a, b, m, d):
    dict_b = {}
    dict_diff_ab = {}
    for i in range(n):
        if a[i] != b[i]:
            dict_diff_ab.setdefault(b[i], 0)
            dict_diff_ab[b[i]] += 1
        dict_b.setdefault(b[i], 0)
        dict_b[b[i]] += 1
    if d[-1] not in dict_b:
        return "No"
    for i in range(m):
        if d[i] in dict_diff_ab:
            dict_diff_ab[d[i]] -= 1
            if dict_diff_ab[d[i]] == 0:
                dict_diff_ab.pop(d[i])
    if len(dict_diff_ab) == 0:
        return "Yes"
    return "No"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    print(solve(n, a, b, m, d))
