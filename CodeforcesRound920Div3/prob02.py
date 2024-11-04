# B. Arranging Cats
def solve(n, s, f):
    s_diff_f = 0
    f_diff_s = 0
    for i in range(n):
        if s[i] != f[i]:
            if s[i] == "1":
                s_diff_f += 1
            else:
                f_diff_s += 1
    large = max(s_diff_f, f_diff_s)
    return large


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    f = input()
    print(solve(n, s, f))
