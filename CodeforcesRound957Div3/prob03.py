# C. Gorilla and Permutation
def solve(n, m, k):
    result = []
    for i in range(n, k - 1, -1):
        result.append(i)
    for i in range(m + 1, k):
        result.append(i)
    for i in range(1, m + 1):
        result.append(i)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
