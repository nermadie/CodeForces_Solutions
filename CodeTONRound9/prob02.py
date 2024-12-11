# B. Shohag Loves Strings
def solve(s):
    for i in range(len(s) - 1):  # aa
        if s[i] == s[i + 1]:
            return s[i] + s[i + 1]
    for i in range(len(s) - 2):  # abc != aba
        if s[i] != s[i + 2]:
            return s[i : i + 3]
    return -1


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
