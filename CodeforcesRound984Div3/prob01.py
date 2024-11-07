# A. Quintomania
def solve(n, a):
    for i in range(n - 1):
        if not (abs(a[i + 1] - a[i]) == 5 or abs(a[i + 1] - a[i]) == 7):
            return "No"
    return "Yes"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
