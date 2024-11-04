def helper(b, q):
    m = [[0] * 7 for _ in range(7)]
    count = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if (i + j) % 2 == q:
                if (
                    b[i][j] == "B"
                    and b[i - 1][j - 1] == "B"
                    and b[i - 1][j + 1] == "B"
                    and b[i + 1][j - 1] == "B"
                    and b[i + 1][j + 1] == "B"
                ):
                    t = 1 << count
                    m[i][j] |= t
                    m[i - 1][j - 1] |= t
                    m[i - 1][j + 1] |= t
                    m[i + 1][j - 1] |= t
                    m[i + 1][j + 1] |= t
                    count += 1
    for item in m:
        print(item)
    m2 = [False] * (1 << count)
    moves = []
    for x in m:
        for y in x:
            if not m2[y]:
                m2[y] = True
                moves.append(y)

    moves2 = []
    for i in range(len(moves)):
        ok = True
        a = moves[i]
        for j in range(len(moves)):
            if i == j:
                continue
            b = moves[j]
            if b & a == a:
                ok = False
                break
        if ok:
            moves2.append(a)
    print("move: ", moves)
    print("move2: ", moves2)

    dp = [20] * (1 << count)  # 20 > 12 hoac 13
    dp[0] = 0
    for i in range(1 << count):
        if dp[i] == 20:
            continue
        for m in moves2:
            t = i | m
            dp[t] = min(dp[t], dp[i] + 1)
    print(dp)
    print()
    return dp[-1]


for _ in range(int(input())):
    b = [list(input()) for _ in range(7)]
    print(helper(b, 0) + helper(b, 1))
