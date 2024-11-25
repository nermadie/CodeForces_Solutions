# C. Penchick and BBQ Buns
def solve(n):
    if n % 2 == 0:
        result = []
        for i in range(n // 2):
            result.append(i + 1)
            result.append(i + 1)
        return " ".join(map(str, result))
    elif n < 26:
        return -1
    else:
        result = [1]
        for i in range(2, 6):
            result.append(i)
            result.append(i)
        result.append(1)
        for i in range(6, 12):
            result.append(i)
            result.append(i)
        result.append(12)
        result.append(13)
        result.append(13)
        result.append(1)
        result.append(12)
        for i in range((n - 27) // 2):
            result.append(i + 14)
            result.append(i + 14)
        return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
