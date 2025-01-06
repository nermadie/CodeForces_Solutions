# B. Make Majority
def solve(n, s):
    if n == 1:
        return "YES" if s == "1" else "NO"
    cnt1 = 0
    cnt0 = 0
    prev = None
    for i in range(n):
        if s[i] == "0" and prev != "0":
            cnt0 += 1
        elif s[i] == "1":
            cnt1 += 1
        prev = s[i]
    if cnt1 > cnt0:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
