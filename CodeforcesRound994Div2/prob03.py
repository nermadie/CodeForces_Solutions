# C. MEX Cycle
def solve(n, x, y):
    result = []
    if y - x == 1 or x + n - y == 1:
        if n % 2 == 1:
            result.append(2)
            for i in range(2, n + 1):
                result.append(i % 2)
        else:
            for i in range(1, n + 1):
                result.append(i % 2)
    else:
        right = y - x - 1
        left = n - y + x - 1
        if right % 2 == 0 and left % 2 == 0:
            for i in range(1, n + 1):
                result.append(i % 2)
        elif right % 2 == 0 or left % 2 == 0:
            if x % 2 == 1:
                for i in range(1, x):
                    result.append(i % 2)
                result.append(2)
                for i in range(x + 1, n + 1):
                    result.append(1 - i % 2)
            else:
                for i in range(1, x):
                    result.append(1 - i % 2)
                result.append(2)
                for i in range(x + 1, n + 1):
                    result.append(i % 2)
        else:
            for i in range(1, n + 1):
                if i == x:
                    result.append(2)
                else:
                    result.append(i % 2)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print(solve(n, x, y))
