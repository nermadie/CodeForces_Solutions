# Points and Minimum Distance
def minimum_path_length(n, a):
    a.sort()
    min_length = a[2 * n - 1] - a[0] - a[n] + a[n - 1]
    path = []
    for i in range(n):
        path.append((a[n + i], a[n - 1 - i]))
    return (min_length, path)


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min_length, path = minimum_path_length(n, a)

    print(min_length)

    for x, y in path:
        print(x, y)
