# B. Battle for Survive
def solve(n, a):
    if n > 2:
        temp_sum = 0
        for i in range(n - 2):
            temp_sum += a[i]
        return a[-1] - a[-2] + temp_sum

    else:
        return a[1] - a[0]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
