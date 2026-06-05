# B. Another Sorting Problem
def solve(n, a):
    down_trend = False
    start_down_trend = 0
    diff_down_trend = 0
    for i in range(1, n):
        if a[i] < a[i - 1]:
            diff_down_trend = max(a[i - 1] - a[i], diff_down_trend)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            if down_trend:
                return "NO"
            else:
                down_trend = True
                start_down_trend = a[i - 1]
        else:
            if down_trend:
                if a[i] - a[i - 1] >= diff_down_trend and a[i] >= start_down_trend:
                    down_trend = False
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
