# B. Preparing for the Contest
def solve(n, k):
    for i in range(n, k + 1, -1):
        print(i, end=" ")
    for i in range(1, k + 2):
        print(i, end=" ")
    print()


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
