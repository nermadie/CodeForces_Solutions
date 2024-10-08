# C. Robin Hood in Town
def solve(n, a):
    if n <= 2:
        return -1
    a.sort()
    total_a = sum(a)
    mid_pos = n // 2
    return 0 if a[mid_pos] * n * 2 < total_a else a[mid_pos] * n * 2 - total_a + 1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
