# B. Above the Clouds
def solve(n, s):
    dict_count = {}
    for i in range(n):
        dict_count.setdefault(s[i], 0)
        dict_count[s[i]] += 1
        if dict_count[s[i]] > 1 and i != len(s) - 1:
            return "YES"
        if dict_count[s[i]] == 2 and i == len(s) - 1:
            if s[0] != s[i]:
                return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
