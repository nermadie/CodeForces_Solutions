# E. Secret Box
def solve(x, y, z, k):
    x, y, z = sorted([x, y, z])
    result = 0
    for i in range(1, x + 1):
        if i > k:
            break
        for j in range(1, y + 1):
            if i * j > k:
                break
            l = k / (j * i)
            if l.is_integer():
                result = max(result, (x - i + 1) * (y - j + 1) * (z - int(l) + 1))
    return result


t = int(input())
for _ in range(t):
    x, y, z, k = map(int, input().split())
    print(solve(x, y, z, k))
