# F. Vlad and Avoiding X
def solve(grid, odd):
    grid_overlapped = [[0] * 7 for _ in range(7)]
    count = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if (i + j) % 2 == odd:
                if (
                    grid[i][j] == "B"
                    and grid[i - 1][j - 1] == "B"
                    and grid[i - 1][j + 1] == "B"
                    and grid[i + 1][j - 1] == "B"
                    and grid[i + 1][j + 1] == "B"
                ):
                    t = 1 << count
                    grid_overlapped[i][j] |= t
                    grid_overlapped[i - 1][j - 1] |= t
                    grid_overlapped[i - 1][j + 1] |= t
                    grid_overlapped[i + 1][j - 1] |= t
                    grid_overlapped[i + 1][j + 1] |= t
                    count += 1
    moves_set = set()
    for i in range(7):
        for j in range(7):
            if grid_overlapped[i][j] not in moves_set and grid_overlapped[i][j] != 0:
                moves_set.add(grid_overlapped[i][j])
    moves_cover_another_moves = set()
    for move_i in moves_set:
        cover_all = True
        for move_j in moves_set:
            if move_i == move_j:
                continue
            if move_j & move_i == move_i:
                cover_all = False
                break
        if cover_all:
            moves_cover_another_moves.add(move_i)
    dp = [20] * (1 << count)
    dp[0] = 0
    for i in range(1 << count):
        if dp[i] == 20:
            continue
        else:
            for move in moves_cover_another_moves:
                state = i | move
                dp[state] = min(dp[state], dp[i] + 1)

    return dp[-1]


t = int(input())
for i in range(t):
    grid = [input() for _ in range(7)]
    print(solve(grid, 1) + solve(grid, 0))
