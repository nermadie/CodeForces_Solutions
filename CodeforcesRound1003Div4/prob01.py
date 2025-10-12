# A. Skibidus and Amog'u
def solve(s):
    return s[:-2] + "i"


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
