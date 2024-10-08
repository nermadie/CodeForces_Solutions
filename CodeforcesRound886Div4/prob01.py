# To My Critics
def solve(a):
    for i in range(3):
        for j in range(i + 1, 3):
            if a[i] + a[j] >= 10:
                return "Yes"
    return "No"


t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    print(solve(a))
