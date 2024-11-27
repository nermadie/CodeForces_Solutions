# D. Sharky Surfing
from hmac import new


def solve(n, m, L, lr, xv):
    result = 0
    cur_max_len_hurdle = -1
    hurdles = []
    for i in range(n):
        if lr[i][1] - lr[i][0] > cur_max_len_hurdle:
            cur_max_len_hurdle = lr[i][1] - lr[i][0]
            hurdles.append((lr[i][0], lr[i][1]))
    cur_power_ups = []
    cur_power = 1
    start_index = 0
    for hurdle in hurdles:
        new_power_ups = []
        for i in range(start_index, m):
            if xv[i][0] >= hurdle[0]:
                break
            start_index = i + 1
            new_power_ups.append(xv[i][1])
        new_power_ups.sort(reverse=True)
        cur_power_ups.extend(new_power_ups)
        cur_power_ups.sort(reverse=True)
        if cur_power < hurdle[1] - hurdle[0] + 2:
            for i in range(len(cur_power_ups)):
                cur_power += cur_power_ups[i]
                result += 1
                if cur_power >= hurdle[1] - hurdle[0] + 2:
                    cur_power_ups = cur_power_ups[i + 1 :]
                    break
            if cur_power < hurdle[1] - hurdle[0] + 2:
                return -1
    # print("cur_power", cur_power)
    return result


t = int(input())
for _ in range(t):
    n, m, L = list(map(int, input().split()))
    lr = []
    for _ in range(n):
        lr.append(list(map(int, input().split())))
    xv = []
    for _ in range(m):
        xv.append(list(map(int, input().split())))
    print(solve(n, m, L, lr, xv))
