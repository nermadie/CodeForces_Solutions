def solve(n):
    result = [0] * n
    if n > 3:
        result[0] = 4
        result[3] = 1
    else:
        return -1
    index = 1
    for i in range(1, n + 1):
        if index == 3:
            index += 1
            continue
        if i != 1 and i != 4:
            result[index] = i
            index += 1

    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
