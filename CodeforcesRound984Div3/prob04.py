# D. I Love 1543
def get_coordinates(n, m, layer, pos):
    if pos >= (m - 2 * layer):
        pos -= m - 2 * layer - 1
    else:
        return (layer, pos + layer - 1)
    if pos >= (n - 2 * layer):
        pos -= n - 2 * layer - 1
    else:
        return (pos + layer - 1, m - layer - 1)
    if pos >= (m - 2 * layer):
        pos -= m - 2 * layer - 1
    else:
        return (n - layer - 1, m - pos - layer)
    return (n - pos - layer, layer)


def solve(n, m, grid):
    num_of_layers = min(n, m) // 2
    result = 0
    for layer in range(num_of_layers):
        num_of_start_pos = 2 * (n + m - 4 * layer) - 4
        for start_pos in range(1, num_of_start_pos + 1):
            coord1 = get_coordinates(n, m, layer, start_pos)
            coord2 = get_coordinates(n, m, layer, start_pos % num_of_start_pos + 1)
            coord3 = get_coordinates(
                n, m, layer, (start_pos + 1) % num_of_start_pos + 1
            )
            coord4 = get_coordinates(
                n, m, layer, (start_pos + 2) % num_of_start_pos + 1
            )

            if (
                grid[coord1[0]][coord1[1]] == "1"
                and grid[coord2[0]][coord2[1]] == "5"
                and grid[coord3[0]][coord3[1]] == "4"
                and grid[coord4[0]][coord4[1]] == "3"
            ):
                result += 1
    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    print(solve(n, m, grid))
