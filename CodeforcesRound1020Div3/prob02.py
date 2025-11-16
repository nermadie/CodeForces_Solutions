# B. St. Chroma
def solve(n, x):
    result = []
    result += [str(i) for i in range(x)]
    result += [str(i) for i in range(x + 1, n)]
    if x < n:
        result.append(str(x))
    return " ".join(result)


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print(solve(n, x))
