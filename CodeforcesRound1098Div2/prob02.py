# B. Remilia Plays Soku
def solve(n, x1, x2, k):
    if n > 3:
        return k + min(abs(x1 - x2), n - abs(x1 - x2))
    else:
        return 1


t = int(input())
for _ in range(t):
    n, x1, x2, k = map(int, input().split())
    print(solve(n, x1, x2, k))
