# D. Inaccurate Subsequence Search
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input().split()
    b = input().split()
    dict_b = {}
    satisfiable = 0
    result = 0
    for i in b:
        dict_b.setdefault(i, 0)
        dict_b[i] += 1
    for i in range(m):
        if a[i] in dict_b:
            if dict_b[a[i]] > 0:
                satisfiable += 1
            dict_b[a[i]] -= 1
    if satisfiable >= k:
        result += 1
    left = 0
    right = m
    while right < n:
        if a[left] in dict_b:
            if dict_b[a[left]] >= 0:
                satisfiable -= 1
            dict_b[a[left]] += 1
        left += 1
        if a[right] in dict_b:
            if dict_b[a[right]] > 0:
                satisfiable += 1
            dict_b[a[right]] -= 1
        right += 1
        if satisfiable >= k:
            result += 1
    print(result)
