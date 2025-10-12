# B. Journey
def solve(n, a, b, c):
    at_least_day = n // (a + b + c)
    n = n % (a + b + c)
    result = 3 * (at_least_day)
    if n > a + b:
        return result + 3
    elif n > a:
        return result + 2
    elif n > 0:
        return result + 1
    else:
        return result


t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    print(solve(n, a, b, c))
