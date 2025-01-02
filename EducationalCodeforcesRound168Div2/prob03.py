# C. Even Positions
def solve(n, s):
    result = 0
    for i in range(n):
        if s[i] == "(":
            result += 1
    return result * 2 + n // 2


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
