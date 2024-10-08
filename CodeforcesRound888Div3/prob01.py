# Escalator Conversations
def conversations_on_escalator(n, m, k, H, heights):
    count = 0
    for height in heights:
        diff_height = abs(height - H)
        if diff_height % k == 0:
            if 0 < diff_height // k < m:
                count += 1
    return count


t = int(input())

for _ in range(t):
    n, m, k, H = map(int, input().split())
    heights = list(map(int, input().split()))
    result = conversations_on_escalator(n, m, k, H, heights)
    print(result)
