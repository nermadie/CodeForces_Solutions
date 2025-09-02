def solve(n):
    result = 9
    for c in n:
        result = min(result, int(c))
    return result


t = int(input())
for _ in range(t):
    n = input()
    print(solve(n))
