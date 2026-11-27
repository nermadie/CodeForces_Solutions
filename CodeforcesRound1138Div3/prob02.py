# B1. Yukari Yakumo and the Boundary Stones (Easy Version)
def solve(x, y, m, s):
    cur_max = x + y
    for i in range(m):
        if s[i] == "-":
            if y > 1:
                y -= 1
                x += 1
            elif x > 0:
                x -= 1
            elif y == 1:
                x += 1
                y -= 1
            else:
                return cur_max
        elif s[i] == "+":
            if y > 0:
                y += 1
            elif x > 0:
                x -= 1
                y += 1
        cur_max = max(cur_max, x + y)
    return cur_max


t = int(input())
for _ in range(t):
    x, y, m = map(int, input().split())
    s = input()
    print(solve(x, y, m, s))
