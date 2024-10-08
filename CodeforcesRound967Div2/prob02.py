# B. Generate Permutation
def solve(n):
    if n % 2 == 0:
        return -1
    else:
        result = []
        result.extend([str(i) for i in range(n // 2 + 1, 0, -1)])
        result.extend([str(i) for i in range(n // 2 + 2, n + 1)])
        return " ".join(result)


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
