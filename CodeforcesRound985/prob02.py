# B. Replacement
def solve(n, s, r):
    cntr0 = r[:-1].count("0")
    cntr1 = n - 2 - cntr0
    cnts0 = s.count("0")
    cnts1 = n - cnts0
    if cntr0 + cnts0 == cntr1 + cnts1:
        if "01" in s or "10" in s:
            return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    r = input()
    print(solve(n, s, r))
