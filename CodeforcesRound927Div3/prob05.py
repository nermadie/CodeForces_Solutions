# E. Final Countdown
def solve(n, s):
    pos_start = -1
    for i in range(n):
        if s[i] != "0":
            pos_start = i
            break
    sum_num = 0
    sum_num_list = [0] * (n - pos_start + 1)
    for i in range(pos_start, n):
        cur_num = int(s[i])
        sum_num += cur_num
        sum_num_list[i - pos_start + 1] = sum_num
    for i in range(len(sum_num_list) - 1, 0, -1):
        sum_num_list[i - 1] += sum_num_list[i] // 10
        sum_num_list[i] %= 10
    if sum_num_list[0] == 0:
        return "".join(map(str, sum_num_list[1:]))
    else:
        return "".join(map(str, sum_num_list))


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
