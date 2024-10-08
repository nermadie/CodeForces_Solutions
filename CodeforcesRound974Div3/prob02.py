# B. Robin Hood and the Major Oak
def solve(n, k):
    first_year = n - k + 1
    temp = (n + first_year) * (n - first_year + 1) // 2
    if temp % 2 == 0:
        return "Yes"
    else:
        return "No"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
