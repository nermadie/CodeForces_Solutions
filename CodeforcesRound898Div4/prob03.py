# Target Practice
def calculate_points(grid):
    total_points = 0

    for i in range(9):
        for j in range(i, 9 - i):
            if grid[i][j] == "X":
                total_points += i + 1
            if grid[j][9 - i] == "X":
                total_points += i + 1
            if grid[9 - i][9 - j] == "X":
                total_points += i + 1
            if grid[9 - j][i] == "X":
                total_points += i + 1

    return total_points


t = int(input())

for _ in range(t):
    grid = [input().strip() for _ in range(10)]
    result = calculate_points(grid)
    print(result)
