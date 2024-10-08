# D. Manhattan Circle
def solve(n, m, matrix):
    max_line, pos_in_first_line = 0, 0
    max_count = 0
    check_first = True
    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[i][j] == "#":
                count += 1
                if check_first:
                    pos_in_first_line = j
                    check_first = False
        if count > max_count:
            max_line = i
            max_count = count
    return str(max_line + 1) + " " + str(pos_in_first_line + 1)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(input())
    print(solve(n, m, matrix))
