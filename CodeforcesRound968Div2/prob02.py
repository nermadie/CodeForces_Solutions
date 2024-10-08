# B. Turtle and Piggy Are Playing a Game 2
def solve(n, a):
    a.sort()
    return a[n // 2]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
