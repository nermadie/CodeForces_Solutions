# A. Penchick and Modern Monument
def solve(n, h):
    longest_same = 1
    cur_same = 1
    for i in range(n - 1):
        if h[i] == h[i + 1]:
            cur_same += 1
        else:
            longest_same = max(longest_same, cur_same)
            cur_same = 1
    longest_same = max(longest_same, cur_same)
    return n - longest_same


t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(solve(n, h))
