# A. Ideal Generator
def solve(k):
    if k % 2 == 0:
        return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    k = int(input())
    print(solve(k))
