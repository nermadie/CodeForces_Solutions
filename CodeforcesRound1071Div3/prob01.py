def solve(i, j):
    return i * j + 1


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(solve(a, b))
