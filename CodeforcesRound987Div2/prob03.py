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
        prefix = "1 3 3 4 4 5 5 6 6 1 2 7 7 8 8 9 9 10 10 11 11 12 12 13 13 1 2 "
        result = []
        for i in range((n - 27) // 2):
            result.append(i + 14)
            result.append(i + 14)
        return prefix + " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
