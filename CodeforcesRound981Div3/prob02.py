# B. Sakurako and Water
def solve(n, a):
    result = 0
    for i in range(n):
        row = i
        col = 0
        min_line = 100000
        while row < n and col < n:
            if a[row][col] < min_line:
                min_line = a[row][col]
            row += 1
            col += 1
        result -= min_line if min_line < 0 else 0
    for i in range(1, n):
        row = 0
        col = i
        min_line = 100000
        while row < n and col < n:
            if a[row][col] < min_line:
                min_line = a[row][col]
            row += 1
            col += 1
        result -= min_line if min_line < 0 else 0
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    print(solve(n, a))
