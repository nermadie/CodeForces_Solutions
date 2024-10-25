# A. Phone Desktop
def solve(x, y):
    min_screen_y = 0
    if y % 2 != 0:
        min_screen_y = y // 2 + 1
    else:
        min_screen_y = y // 2
    remainder = 15 * min_screen_y - y * 4
    min_screen_all = min_screen_y
    if x >= remainder:
        min_screen_all += (x - remainder) // 15
        if (x - remainder) % 15 != 0:
            min_screen_all += 1
    return min_screen_all
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(solve(x, y))