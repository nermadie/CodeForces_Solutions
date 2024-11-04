# F. Vlad and Avoiding X
def get_even_center(grid):
    even_center = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if (i + j) % 2 == 0 and grid[i - 1][j - 1] + grid[i - 1][j + 1] + grid[
                i + 1
            ][j - 1] + grid[i + 1][j + 1] + grid[i][j] == 5:
                even_center += 1
    return even_center


def get_odd_center(grid):
    odd_center = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if (i + j) % 2 == 1 and grid[i - 1][j - 1] + grid[i - 1][j + 1] + grid[
                i + 1
            ][j - 1] + grid[i + 1][j + 1] + grid[i][j] == 5:
                odd_center += 1
    return odd_center


def solve(grid):
    temp_grid = [[0] * 7 for _ in range(7)]
    for i in range(7):
        for j in range(7):
            temp_grid[i][j] = 1 if grid[i][j] == "B" else 0
    grid = temp_grid
    odd_center = []
    even_center = []
    for i in range(1, 6):
        for j in range(1, 6):
            if (
                grid[i][j] == 1
                and grid[i - 1][j - 1] == 1
                and grid[i - 1][j + 1] == 1
                and grid[i + 1][j - 1] == 1
                and grid[i + 1][j + 1] == 1
            ):
                if (i + j) % 2 == 0:
                    even_center.append((i, j))
                else:
                    odd_center.append((i, j))
    min_even = 4
    min_odd = 4
    even_case = [(i, j) for i in range(1, 6) for j in range(1, 6) if (i + j) % 2 == 0]
    odd_case = [(i, j) for i in range(1, 6) for j in range(1, 6) if (i + j) % 2 == 1]
    dp_even = [[0] * (1 << 13) for _ in range(len(even_center))]
    dp_odd = [[0] * (1 << 12) for _ in range(len(odd_center))]
    # (i + j) % 2 == 0 EVEN
    for i in range(1 << 13):
        bitmask = bin(i)[2:].zfill(13)
        operation_point = []
        for i in range(len(bitmask)):
            if bitmask[i] == "1":
                operation_point.append(even_case[i])
        prev_black = []
        for item in operation_point:
            if grid[item[0]][item[1]] == 1:
                prev_black.append(item)
            grid[item[0]][item[1]] = 0
        if get_even_center(grid) == 0 and len(operation_point) < min_even:
            min_even = len(operation_point)
        for item in prev_black:
            grid[item[0]][item[1]] = 1
    # (i + j) % 2 == 1 ODD
    for i in range(1 << 12):
        bitmask = bin(i)[2:].zfill(12)
        operation_point = []
        for j in range(len(bitmask)):
            if bitmask[j] == "1":
                operation_point.append(odd_case[j])
        prev_black = []
        for item in operation_point:
            if grid[item[0]][item[1]] == 1:
                prev_black.append(item)
            grid[item[0]][item[1]] = 0
        if get_odd_center(grid) == 0 and len(operation_point) < min_odd:
            min_odd = len(operation_point)
        for item in prev_black:
            grid[item[0]][item[1]] = 1
    return min_even + min_odd


t = int(input())
for i in range(t):
    grid = [input() for _ in range(7)]
    print(solve(grid))
