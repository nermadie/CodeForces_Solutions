# C. Action Figures
def solve(n, s):
    if n == 1:
        return 1
    money_spend = ((1 + n) * n // 2) - n
    count = 1
    pos = n - 2
    while pos > count:
        if s[pos] == "1":
            money_spend -= pos + 1
            count += 1
        else:
            if count > 0:
                count -= 1
        pos -= 1

    return money_spend


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
