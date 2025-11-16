# C. Simple Repetition
def solve(x, k):
    if x == 1:
        if k == 2:
            return "YES"
        else:
            return "NO"
    if x == 2 and k == 1:
        return "YES"
    if k > 1:
        return "NO"
    if x % 2 == 0:
        return "NO"
    for i in range(3, x, 2):
        if i * i > x:
            break
        if x % i == 0:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    print(solve(x, k))
