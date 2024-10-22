def solve(n, gw_list):
    connected_list = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if gw_list[i][0] == gw_list[j][0] or gw_list[i][1] == gw_list[j][1]:
                connected_list[i].add(j)
                connected_list[j].add(i)
    dp = [[(1 if i == 2**j else 0) for j in range(n)] for i in range(2**n)]
    for i in range(2**n):
        for j in range(n):
            if i & (2**j):
                for k in range(n):
                    dp[i][j] |= dp[i - (2**j)][k] & int(k in connected_list[j])
    return n - max([(bin(i).count("1") if sum(dp[i]) else 0) for i in range(2**n)])


t = int(input())
for _ in range(t):
    n = int(input())
    gw_list = []
    for _ in range(n):
        g, w = input().split()
        gw_list.append((g, w))

    print(solve(n, gw_list))
