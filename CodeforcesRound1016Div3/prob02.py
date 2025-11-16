# B. Expensive Number
def solve(n):
    result = 0
    cnt_zero_from_last_diff_zero = 0
    for i in range(len(n)):
        cur_digit = int(n[i])
        if cur_digit != 0:
            result += 1
            cnt_zero_from_last_diff_zero = 0
        else:
            cnt_zero_from_last_diff_zero += 1
    return result + cnt_zero_from_last_diff_zero - 1


t = int(input())
for _ in range(t):
    n = input()
    print(solve(n))
