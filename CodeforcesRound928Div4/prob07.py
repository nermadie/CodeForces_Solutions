# G. Vlad and Trouble at MIT
def solve(n, a, s):
    dps = [0] * n
    dpp = [0] * n
    for i in range(n)[::-1]:
        if s[i] == "S":
            dpp[i] = float("inf")
        if s[i] == "P":
            dps[i] = float("inf")
        if i > 0:
            dpp[a[i - 1] - 1] += min(dpp[i], dps[i] + 1)
            dps[a[i - 1] - 1] += min(dps[i], dpp[i] + 1)
    return min(dps[0], dpp[0])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    print(solve(n, a, s))
