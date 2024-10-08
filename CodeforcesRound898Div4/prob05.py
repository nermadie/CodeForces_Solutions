# Building an Aquarium
def max_tank_height(n, x, heights):
    max_height_possible = x + 1000000000
    low = 0
    high = max_height_possible
    while low < high:
        mid = (low + high) // 2
        total = 0
        for i in range(n):
            total += max(0, mid - heights[i])
        if total <= x:
            low = mid + 1
        else:
            high = mid - 1
    last_total = 0
    last_height = (low + high) // 2
    for i in range(n):
        last_total += max(0, last_height - heights[i])
    return last_height - 1 if last_total > x else last_height


t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    heights = list(map(int, input().split()))
    print(max_tank_height(n, x, heights))
