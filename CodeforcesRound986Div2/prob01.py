# A. Alice's Adventures in "Chess"
def solve(n, a, b, s):
    cur_pos = (0, 0)
    i = 0
    attempt = 0
    while True:
        if s[i] == "N":
            cur_pos = (cur_pos[0], cur_pos[1] + 1)
        elif s[i] == "S":
            cur_pos = (cur_pos[0], cur_pos[1] - 1)
        elif s[i] == "W":
            cur_pos = (cur_pos[0] - 1, cur_pos[1])
        elif s[i] == "E":
            cur_pos = (cur_pos[0] + 1, cur_pos[1])
        if cur_pos == (a, b):
            return "YES"
        i += 1
        if i == n:
            i %= n
            attempt += 1
            if attempt == 20:
                break
    return "NO"


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()
    print(solve(n, a, b, s))
