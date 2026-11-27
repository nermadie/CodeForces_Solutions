# A. Youmu Konpaku and the Duel
x_result = [0] * 250
for i in range(1, 250):
    cur_max = 0
    for j in range(i):
        right_bound = j + 1
        attack = i - j
        left_bound = right_bound - attack + 1
        total = ((right_bound + left_bound) * attack) // 2
        cur_max = max(cur_max, total)
    x_result[i] = cur_max


def solve(x):
    for i in range(250):
        if x_result[i] >= x:
            return i


t = int(input())
for _ in range(t):
    x = int(input())
    print(solve(x))
