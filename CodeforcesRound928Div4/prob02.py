# B. Vlad and Shapes
def find_shape(grid):
    check_first = False
    first_len = 0
    second_len = 0
    for i in range(len(grid)):
        if first_len != 0:
            check_first = True
        if second_len != 0:
            if first_len != second_len:
                return 'TRIANGLE'
            else:
                return 'SQUARE'
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and check_first == False:
                first_len += 1
            elif grid[i][j] == '1' and check_first == True:
                second_len += 1
    if first_len != second_len:
        return 'TRIANGLE'
    else:
        return 'SQUARE'


t = int(input())
for _ in range(t):
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    print(find_shape(grid))
