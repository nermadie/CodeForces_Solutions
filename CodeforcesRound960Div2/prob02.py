# B. Array Craft
def solve(n, x, y):
    result = []
    if y % 2 == 0:
        for i in range(1, y):
            if i % 2 == 1:
                result.append("-1")
            else:
                result.append("1")
    else:
        for i in range(1, y):
            if i % 2 == 1:
                result.append("1")
            else:
                result.append("-1")
    result.extend(["1"] * (x - y + 1))
    for i in range(x + 1, n + 1):
        if (i - x) % 2 == 1:
            result.append("-1")
        else:
            result.append("1")
    return " ".join(result)


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print(solve(n, x, y))
