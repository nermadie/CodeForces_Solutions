def solve(a, b, x):
    result = 0
    temp = 100000
    while a != b:
        a, b = (max(a, b), min(a, b))
        div = a // x
        if div == b:
            result += 1
            break
        if div > b:
            a = div
            result += 1
        if div < b:
            temp = min(a - b + result, temp)
            a = div
            result += 1
    return min(result, temp)

    return result


t = int(input())
for _ in range(t):
    a, b, x = map(int, input().split())
    print(solve(a, b, x))
