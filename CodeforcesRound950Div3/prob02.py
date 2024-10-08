# B. Choosing Cubes
def solve(n, f, k, a):
    favourite = a[f - 1]
    a.sort(reverse=True)
    a = a[k - 1 :]
    if len(a) <= 1:
        return "Yes"
    if a[0] == a[1] == favourite:
        return "Maybe"
    if a[1] >= favourite:
        return "No"
    else:
        return "Yes"


t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, f, k, a))
