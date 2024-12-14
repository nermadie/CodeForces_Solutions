# A. Find K Distinct Points with Fixed Center
def solve(xc, yc, k):
    result = []
    if k % 2 == 1:
        result.append((xc, yc))
    for i in range(1, (k // 2) + 1):
        result.append((xc + i, yc))
        result.append((xc - i, yc))
    return result


t = int(input())
for _ in range(t):
    xc, yc, k = map(int, input().split())
    arr = solve(xc, yc, k)
    for x, y in arr:
        print(x, y)
