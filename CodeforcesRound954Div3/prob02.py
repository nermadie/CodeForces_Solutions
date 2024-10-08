# B. Matrix Stabilization
def solve(n, m, matrix):
    for i in range(n):
        for j in range(m):
            top = matrix[i - 1][j] if i > 0 else 0
            left = matrix[i][j - 1] if j > 0 else 0
            right = matrix[i][j + 1] if j < m - 1 else 0
            bottom = matrix[i + 1][j] if i < n - 1 else 0
            max_val = max(top, left, right, bottom)
            matrix[i][j] = min(matrix[i][j], max_val)
    return matrix


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    matrix = solve(n, m, matrix)
    for row in matrix:
        print(" ".join(map(str, row)))
