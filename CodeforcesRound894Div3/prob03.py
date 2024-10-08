# Flower City Fence
def is_symmetrical_fence(n, heights):
    if n != heights[0]:
        return "NO"
    if n == 1:
        if heights[0] == 1:
            return "YES"
        else:
            return "NO"
    right = n - 1
    count1 = 1
    for left in range(1, n):
        if heights[left] != heights[left - 1]:
            if heights[right] != count1:
                return "NO"
            diff = heights[left - 1] - heights[left]
            count = 1
            while left < right and heights[right] == heights[right - 1]:
                count += 1
                right -= 1
            right -= 1
            if count != diff:
                return "NO"
        count1 += 1
        if heights[left] <= left + 1 or left == right:
            break

    return "YES"


t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))

    print(is_symmetrical_fence(n, heights))
