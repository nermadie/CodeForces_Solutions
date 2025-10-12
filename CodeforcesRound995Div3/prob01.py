# A. Preparing for the Olympiad
def solve(n, a, b):
    result = 0
    for i in range(n - 1):
        if a[i] > b[i + 1]:
            result += a[i] - b[i + 1]
    return result + a[-1]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
