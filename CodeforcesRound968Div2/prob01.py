# A. Turtle and Good Strings
def solve(n, s):
    if s[0] == s[n - 1]:
        return "No"
    else:
        return "Yes"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
