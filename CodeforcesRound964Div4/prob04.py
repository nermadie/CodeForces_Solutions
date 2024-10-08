# D. Slavic's Exam
def solve(s, t):
    result = []
    cur_t_index = 0
    for c in s:
        if cur_t_index == len(t) and c == "?":
            result.append("a")
        elif cur_t_index < len(t) and c == t[cur_t_index] or c == "?":
            result.append(t[cur_t_index])
            cur_t_index += 1
        else:
            result.append(c)
    if cur_t_index < len(t):
        print("NO")
    else:
        print("YES")
        print("".join(result))


t = int(input())
for _ in range(t):
    s = input()
    t = input()
    solve(s, t)
