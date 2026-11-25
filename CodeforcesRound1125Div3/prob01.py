# A. In Search of Convenience
def solve(x, y, R):
    return f"{(x + R)} {y}"


t = int(input())
for _ in range(t):
    x, y, R = map(int, input().split())
    print(solve(x, y, R))
