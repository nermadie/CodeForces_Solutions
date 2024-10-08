# Qingshan Loves Strings 2
def make_good_string(n, s):
    if n % 2 == 1:
        return [-1]
    left = 1
    right = n
    cur_left = s[left - 1]
    cur_right = s[right - 1]
    result = []
    while True:
        if left == n or left + 1 == right:
            if cur_left == cur_right:
                return [-1]
            else:
                result_len = len(result)
                if result_len > 300:
                    return [-1]
                else:
                    return result_len, result
        if cur_left == cur_right:
            if cur_left == "1":
                result.append(left - 1)
                s = s[: left - 1] + "01" + s[left - 1 :]
            else:
                result.append(right)
                s = s[:right] + "01" + s[right:]
            left += 1
            right += 1
        else:
            left += 1
            right -= 1
        cur_left = s[left - 1]
        cur_right = s[right - 1]


t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    result = make_good_string(n, s)

    if result[0] == -1:
        print(result[0])
    else:
        print(result[0])
        print(" ".join(map(str, result[1])))
