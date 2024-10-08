# Qingshan Loves Strings
def is_good_string(n, m, s, t):
    first_t = t[0]
    cur_t = t[0]
    check = False
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            check = True
            if m % 2 == 0:
                return "No"
            if s[i] == first_t:
                return "No"
    if check:
        for i in range(1, m):
            if t[i] == cur_t:
                return "No"
            cur_t = t[i]
    return "Yes"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    t = input().strip()
    print(is_good_string(n, m, s, t))
