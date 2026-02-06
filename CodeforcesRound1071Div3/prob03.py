# C. Blackslex and Number Theory
def solve(n, a):
    min1 = min(a)
    min2 = 1000000000
    for i in range(n):
        if a[i] != min1:
            min2 = min(min2, a[i])
    return max(min1, min2 - min1)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
