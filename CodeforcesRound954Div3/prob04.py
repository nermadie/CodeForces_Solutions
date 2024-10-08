# D. Mathematical Problem
def solve(n, s):
    if n == 2:
        return int(s)

    index = s.find("0")
    if index != -1 and not (index == 1 and n == 3):
        return 0
    sec_min_val = 100
    min_val = 101
    sec_min_index = -1
    min_index = -1
    for i in range(0, n - 1):
        cur_val = int(s[i : i + 2])
        if cur_val < min_val:
            sec_min_val = min_val
            min_val = cur_val
            sec_min_index = min_index
            min_index = i
        elif min_val < cur_val < sec_min_val:
            sec_min_val = cur_val
            sec_min_index = i
    if min_val % 10 == 1 and sec_min_val - min_val < 9:
        min_val = sec_min_val
        min_index = sec_min_index
    s = s[:min_index] + s[min_index + 2 :]
    result = 0
    for i in range(n - 2):
        if result == 0 and s[i] != "1":
            result = int(s[i])
        else:
            if s[i] != "1":
                result += int(s[i])
    if result == 0:
        return min_val
    return min(result * min_val, result + min_val)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
