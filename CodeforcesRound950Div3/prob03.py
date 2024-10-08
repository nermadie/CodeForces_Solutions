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
    dict_d = {}
    for i in range(m):
        dict_d.setdefault(d[i], 0)
        dict_d[d[i]] += 1
    if d[-1] not in dict_b:
        return "No"
    for key, value in dict_diff_ab.items():
        if key not in dict_d:
            return "No"
        if dict_d[key] < value:
            return "No"
    return "Yes"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    print(solve(n, a, b, m, d))
