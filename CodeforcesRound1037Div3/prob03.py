def solve(n, k, h):
    cur_height = h[k - 1]
    h = sorted(list(set(h)))
    h_index = h.index(cur_height)
    cur_water = 0
    for i in range(h_index + 1, len(h)):
        if h[i - 1] < h[i] - h[i - 1] + cur_water:
            return "NO"
        else:
            cur_water += h[i] - h[i - 1]
    return "YES"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(solve(n, k, h))
