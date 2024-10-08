# The Morning Star
def count_valid_pairs(n, points):
    return points


t = int(input())
for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    result = count_valid_pairs(n, points)
    print(result)
