# A. Little Nikita
def solve(n, m):
    return "YES" if (n - m) % 2 == 0 and n >= m else "NO"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
