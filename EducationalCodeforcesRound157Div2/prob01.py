# Treasure Chest
def smallest_time_to_open_chest(x, y, k):
    if x > y:
        return x
    else:
        if (y - x) - k > 0:
            return ((y - x) - k) * 2 + x + k
        else:
            return y


t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())
    print(smallest_time_to_open_chest(x, y, k))
