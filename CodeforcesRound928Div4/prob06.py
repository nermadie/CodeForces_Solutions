# F. Vlad and Avoiding X
def solve(grid):
    center = set()
    black_pos = [[0] * 7 for i in range(7)]
    for i in range(1, 6):
        for j in range(1, 6):
            if grid[i][j] == "B":
                if (
                    grid[i - 1][j - 1] == "B"
                    and grid[i + 1][j + 1] == "B"
                    and grid[i + 1][j - 1] == "B"
                    and grid[i - 1][j + 1] == "B"
                ):
                    center.add((i, j))
                    black_pos[i][j] += 1
                    black_pos[i - 1][j - 1] += 1
                    black_pos[i + 1][j + 1] += 1
                    black_pos[i + 1][j - 1] += 1
                    black_pos[i - 1][j + 1] += 1

    for i in black_pos:
        print(i)

    result = 0
    while True:
        max_black = 0
        max_pos = (0, 0)
        for i in range(7):
            for j in range(7):
                if black_pos[i][j] > max_black:
                    max_black = black_pos[i][j]
                    max_pos = (i, j)
        if max_black == 0:
            break
        remove_set = set()
        for item in center:
            if (
                (max_pos[0] == item[0] and max_pos[1] == item[1])
                or (max_pos[0] == item[0] + 1 and max_pos[1] == item[1] + 1)
                or (max_pos[0] == item[0] - 1 and max_pos[1] == item[1] - 1)
                or (max_pos[0] == item[0] + 1 and max_pos[1] == item[1] - 1)
                or (max_pos[0] == item[0] - 1 and max_pos[1] == item[1] + 1)
            ):
                remove_set.add(item)
                black_pos[item[0]][item[1]] -= 1
                black_pos[item[0] - 1][item[1] - 1] -= 1
                black_pos[item[0] + 1][item[1] + 1] -= 1
                black_pos[item[0] + 1][item[1] - 1] -= 1
                black_pos[item[0] - 1][item[1] + 1] -= 1
        center -= remove_set
        result += 1
    return result


t = int(input())
for i in range(t):
    grid = [input() for _ in range(7)]
    print(solve(grid))
