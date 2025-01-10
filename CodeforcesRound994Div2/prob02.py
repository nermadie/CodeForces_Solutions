# B. pspspsps
def solve(n, s):
    first_p_index = -1
    last_s_index = n
    for i in range(n):
        if s[i] == "p":
            first_p_index = i
            break
    for i in range(n - 1, -1, -1):
        if s[i] == "s":
            last_s_index = i
            break
    if first_p_index == -1 or last_s_index == n:
        return "YES"
    if first_p_index == n - 1 or last_s_index == 0:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
