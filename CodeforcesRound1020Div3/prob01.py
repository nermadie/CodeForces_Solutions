# A. Dr. TC
def solve(n, s):
    result = 0
    for i in range(n):
        if s[i] == "1":
            result += n - 1
        else:
            result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
