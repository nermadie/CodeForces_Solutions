# XOR Palindromes
def is_good_number(s):
    if len(s) == 1:
        return "11"
    mid = len(s) % 2
    sym_count = 0
    unsym_count = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            sym_count += 1
        else:
            unsym_count += 1
    left_bound = unsym_count
    right_bound = unsym_count + sym_count * 2 + mid
    result = ""
    if mid == 1:
        result += (
            "0" * left_bound
            + "1" * (right_bound - left_bound + 1)
            + "0" * (len(s) - right_bound)
        )
    else:
        result += (
            "0" * left_bound + "1" + "01" * (sym_count) + "0" * (len(s) - right_bound)
        )
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(is_good_number(s))
