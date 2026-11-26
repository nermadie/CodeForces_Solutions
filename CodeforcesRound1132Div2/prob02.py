# A2. 15K4JR3B (Hard Version)
def solve(n, a):
    a.sort()
    a_count = [0] * 25
    for i in range(n):
        a_count[a[i]] += 1

    for i in range(24):
        if a_count[i + 1] % 2 == 1 and a_count[i] >= 2:
            a_count[i] -= 2
            a_count[i + 1] += 1

    width = 0
    height = 0
    is_odd = False

    for i in range(24, -1, -1):
        if is_odd:
            width += (2**i) * a_count[i]
            continue
        if a_count[i] % 2 != 0:
            is_odd = True
            width += (2**i) * (a_count[i] // 2)
            height += (2**i) * ((a_count[i] // 2) + 1)
        else:
            inc = (2**i) * (a_count[i] // 2)
            width += inc
            height += inc

    return width * height


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
