# C. Chipmunk Theo and Equality
def solve(n, a):
    a.sort()
    c1 = {a[0]: 1}
    c2 = {a[0]: 0}
    count = 0
    a0_clone = a[0]
    if a0_clone == 1:
        c1[2] = 1
        c2[2] = 1
    while a0_clone != 1:
        if a0_clone % 2 == 0:
            a0_clone //= 2
        else:
            a0_clone += 1
        count += 1
        c2[a0_clone] = count
        c1[a0_clone] = 1

    for i in range(1, n):
        a_clone = a[i]
        if a_clone == 1:
            c1[1] += 1
            c2[1] += 0
            c1[2] += 1
            c2[2] += 1
            continue
        count = 0
        if a_clone in c1:
            c1[a_clone] += 1
            c2[a_clone] += count
        while a_clone != 1:
            if a_clone % 2 == 0:
                a_clone //= 2
            else:
                a_clone += 1
            count += 1
            if a_clone in c1:
                c1[a_clone] += 1
                c2[a_clone] += count

    result = 99999999999999
    for k, v in c1.items():
        if v == n:
            result = min(result, c2[k])
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
