# Tiles Comeback
def can_construct_path(n, k, colors):
    count = 0
    ref = colors[0]
    left = 0
    while left < n:
        if colors[left] == ref:
            count += 1
            if count == k:
                if left == n - 1 or colors[left] == colors[-1]:
                    return "YES"
                else:
                    break
        left += 1
    count = 0
    ref = colors[-1]
    for right in range(n - 1, left, -1):
        if colors[right] == ref:
            count += 1
            if count == k:
                return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    print(can_construct_path(n, k, colors))
