# B. Skibidus and Ohio
def solve(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 1
    return len(s)


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
