# E. Photoshoot for Gorillas
def solve(n, m, k, w, a):
    a.sort()
    jungle = [0] * m * n
    for i in range(n):
        for j in range(m):
            mul_row = min(i + 1, n - i, k, n - k + 1)
            mul_col = min(j + 1, m - j, k, m - k + 1)
            jungle[i * m + j] = mul_row * mul_col
    jungle.sort()
    result = 0
    for i in range(w):
        result += a[w - i - 1] * jungle[n * m - i - 1]
    return result


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    w = int(input())
    a = list(map(int, input().split()))
    print(solve(n, m, k, w, a))
