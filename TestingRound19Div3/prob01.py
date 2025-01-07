# A. Alternating Sum of Numbers
def solve(n, a):
    result = 0
    for i in range(n):
        result += (-1) ** (i % 2) * a[i]
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
