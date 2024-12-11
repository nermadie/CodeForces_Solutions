# A. Shohag Loves Mod
def solve(n):
    result = []
    for i in range(n):
        result.append((i + 1) + i)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
