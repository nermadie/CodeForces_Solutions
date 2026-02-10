# B. Reverse a Permutation
def solve(n, p):
    index = 0
    for i in range(n):
        if p[i] != n - i:
            index = i
            break

    end_index = -1
    for i in range(n - 1, -1, -1):
        if p[i] == n - index:
            end_index = i
            break

    p[index : end_index + 1] = reversed(p[index : end_index + 1])
    return " ".join(map(str, p))


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
