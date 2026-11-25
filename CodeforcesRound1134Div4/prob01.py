def solve(a, b, c):
    arr = [a, b, c]
    arr.sort()
    if a + 1 == b == c - 1:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
