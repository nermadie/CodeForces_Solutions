# C. Assembly via Remainders
def solve(n, x):
    max_val = max(x)
    result = [max_val + 1]
    for i in range(n - 1):
        result.append(result[-1] + x[i])
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    print(solve(n, x))
