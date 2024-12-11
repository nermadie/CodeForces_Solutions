# A. Sliding
def solve(n, m, r, c):
    row_moves = n - r
    col_moves = n * m - ((r - 1) * m + c) - row_moves
    return row_moves * m + col_moves


t = int(input())
for _ in range(t):
    n, m, r, c = map(int, input().split())
    print(solve(n, m, r, c))
