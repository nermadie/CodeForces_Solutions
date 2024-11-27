# C. Superultra's Favorite Permutation
def solve(n):
    if n <= 4:
        return -1
    result = []
    for i in range(1, n + 1, 2):
        if i != 5:
            result.append(i)
    result.append(5)
    result.append(4)
    for i in range(2, n + 1, 2):
        if i != 4:
            result.append(i)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
