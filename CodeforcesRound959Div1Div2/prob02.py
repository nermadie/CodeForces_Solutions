# B. Fun Game
def solve(n, s, t):
    if s[0] == "0" and t[0] == "1":
        return "NO"
    elif s[0] == "0" and t[0] == "0":
        pattern01_check = False
        for i in range(1, n):
            if s[i] == "1":
                pattern01_check = True
                continue
            if s[i] == "0" and t[i] == "1" and not pattern01_check:
                return "NO"
        return "YES"
    else:
        return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))
