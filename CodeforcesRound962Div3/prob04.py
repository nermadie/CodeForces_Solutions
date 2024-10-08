# D.Fun
# ab + bc + ac <= n
# a + b + c <= x
def solve(n, x):
    result = 0
    for a in range(1, min(n, x)):
        b = 1
        while a * b <= n and a + b <= x:
            result += min((n - a * b) // (a + b), x - a - b)
            b += 1
    return result


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print(solve(n, x))
