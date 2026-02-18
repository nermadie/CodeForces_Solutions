# C. Those Who Are With Us
def solve(n, m, matrix):
    max_val = max([max(row) for row in matrix])
    result_row = -1
    result_col = -1
    options = []
    phase = 0
    first_row = -1
    first_col = -1
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == max_val:
                if phase == 0:
                    first_row = r
                    first_col = c
                    phase = 1
                elif phase == 1:
                    if r != first_row and c != first_col:
                        options.append((first_row, c))
                        options.append((r, first_col))
                        phase = 2
                    elif r == first_row:
                        result_row = r
                        phase = -1
                    elif c == first_col:
                        result_col = c
                        phase = -1
                elif phase == 2:
                    for option in options:
                        if option[0] == r or option[1] == c:
                            result_row = option[0]
                            result_col = option[1]
                            phase = -1
                            break
                    if result_row == -1 and result_col == -1:
                        return max_val

                else:
                    if result_row == -1 and c != result_col:
                        result_row = r
                    elif result_col == -1 and r != result_row:
                        result_col = c
                    elif r != result_row and c != result_col:
                        return max_val

    return max_val - 1


t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    print(solve(n, m, matrix))
