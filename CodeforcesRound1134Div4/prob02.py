def get_new_color(cur_color):
    if cur_color == "R":
        return "B"
    else:
        return "R"


def solve(n, s):
    cur_color = "R"
    result = 0
    for i in range(n):
        if s[i] != cur_color:
            cur_color = get_new_color(cur_color)
            result += 1
        cur_color = get_new_color(cur_color)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
