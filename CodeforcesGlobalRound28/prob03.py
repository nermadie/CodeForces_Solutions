# C. Kevin and Binary Strings
def solve(s):
    max_val = 0
    zero_index = -1
    for i in range(len(s)):
        if s[i] == "0":
            zero_index = i
            break
    if zero_index == -1:
        return " ".join(map(str, [1, len(s), 1, 1]))
    len_2nd_sub = len(s) - zero_index
    start_2nd_index = -1
    for i in range(zero_index):
        cur_xor = int(s[i : len_2nd_sub + i], 2) ^ int(s, 2)
        if max_val < cur_xor:
            max_val = cur_xor
            start_2nd_index = i
    return " ".join(
        map(str, [1, len(s), start_2nd_index + 1, len_2nd_sub + start_2nd_index])
    )


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
