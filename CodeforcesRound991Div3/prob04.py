# D. Digital string maximization
def solve(n):
    i = 1
    while i < len(n):
        if i > 0 and n[i] > n[i - 1] + 1:
            n[i], n[i - 1], i = n[i - 1], n[i] - 1, i - 1
        else:
            i += 1
    return "".join(map(str, n))


t = int(input())
for _ in range(t):
    n = list(map(int, input()))
    print(solve(n))
