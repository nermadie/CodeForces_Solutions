# G. Shuffling Songs
# DP: REACHABLE STATES
#       From Pos    0   1   2   3
# Travelled
# 0000              [False, False, False, False],
# 0001              [True, False, False, False],
# 0010              [False, True, False, False],
# 0011              [False, True, False, False],
# 0100              [True, True, False, False],
# 0101              [True, False, True, False],
# 0110              [False, False, False, False],
# 0111              [False, False, False, False],
# 1000              [False, False, False, True],
# 1001              [False, False, False, False],
# 1010              [False, False, False, False],
# 1011              [False, False, False, False],
# 1100              [False, False, True, True],
# 1101              [True, False, False, True],
# 1110              [False, False, False, False],
# 1111              [False, True, False, True]
#                           ^^^^         ^^^^


def solve(n, gw_list):
    if n == 1:
        return 0
    connected_list = [0 for _ in range(n)]
    for i in range(n):
        cur_val = 0
        for j in range(n):
            if i == j:
                continue
            if gw_list[i][0] == gw_list[j][0] or gw_list[i][1] == gw_list[j][1]:
                cur_val += 2**j
        connected_list[i] = cur_val
    dp = [[(True if 2**j == i else False) for j in range(n)] for i in range(2**n)]
    for i in range(2**n):
        for j in range(n):
            if i & 2**j:
                for k in range(n):
                    if dp[i - 2**j][k] and 2**k & connected_list[j]:
                        dp[i][j] = True
                        break
    if n == 4:
        print(dp)
    max_result = 1
    for i in range(2**n):
        check = False
        for j in range(n):
            if dp[i][j] == True:
                check = True
        if check:
            max_result = max(max_result, bin(i).count("1"))
    return n - max_result


t = int(input())
for _ in range(t):
    n = int(input())
    gw_list = []
    for _ in range(n):
        g, w = input().split()
        gw_list.append((g, w))

    print(solve(n, gw_list))
