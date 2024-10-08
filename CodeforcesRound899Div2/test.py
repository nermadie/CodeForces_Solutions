t = int(input())

for _ in range(t):
    n = int(input())
    num = [0] * 51

    tot = 0
    for i in range(n):
        k, *s = map(int, input().split())
        for x in s:
            num[i] |= 1 << x
        tot |= num[i]

    ans = 0
    for i in range(1, 51):
        if not (tot >> i & 1):
            continue

        cur = 0
        for j in range(n):
            if num[j] >> i & 1:
                continue
            cur |= num[j]

        ans = max(ans, bin(cur).count("1"))
    print(ans)
