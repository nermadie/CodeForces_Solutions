# C - Uninteresting Number
def solve(n):
    sum_digit = 0
    cnt2 = 0
    cnt3 = 0
    for c in n:
        sum_digit += int(c)
        if c == "2":
            cnt2 += 1
        elif c == "3":
            cnt3 += 1
    need = 9 - sum_digit % 9
    if need == 9:
        return "YES"
    if need % 2 == 1:
        need += 9
    need -= min(need // 6, cnt3) * 6
    if need // 2 > cnt2:
        return "NO"
    else:
        return "YES"


t = int(input())
for _ in range(t):
    n = input()
    print(solve(n))
