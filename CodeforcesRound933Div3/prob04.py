# D. Rudolf and the Ball Game
def solve(n, m, x, r):
    dp = set()
    move = int(r[0][0])
    direct = r[0][1]
    if direct == "0":
        dp.add((x + move - 1) % n + 1)
    elif direct == "1":
        dp.add((x - move - 1) % n + 1)
    else:
        dp.add((x + move - 1) % n + 1)
        dp.add((n + x - move - 1) % n + 1)
    for i in range(1, m):
        new_set = set()
        for item in dp:
            move = int(r[i][0])
            direct = r[i][1]
            if direct == "0":
                new_set.add((item + move - 1) % n + 1)
            elif direct == "1":
                new_set.add((item - move - 1) % n + 1)
            else:
                new_set.add((item + move - 1) % n + 1)
                new_set.add((n + item - move - 1) % n + 1)
        dp = new_set
    print(len(dp))
    list_dp = list(dp)
    list_dp.sort()
    print(" ".join(str(i) for i in list_dp))


t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    r = []
    for _ in range(m):
        r.append(input().split())
    solve(n, m, x, r)
