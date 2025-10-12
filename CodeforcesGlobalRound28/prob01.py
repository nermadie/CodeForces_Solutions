# A. Kevin and Combination Lock
def solve(x):
    if x % 33 == 0:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    x = int(input())
    print(solve(x))
