# B. Three Piles
def solve(a, b, c):
    return max(abs(a - b), abs(a + c - b))


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
