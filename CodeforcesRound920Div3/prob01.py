# A. Square
def solve(vertices):
    max_x = -1000
    max_y = -1000
    min_x = 1000
    min_y = 1000
    for vertex in vertices:
        x, y = vertex
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    return (max_x - min_x) * (max_y - min_y)


t = int(input())
for _ in range(t):
    vertices = []
    for _ in range(4):
        x, y = map(int, input().split())
        vertices.append((x, y))
    print(solve(vertices))
