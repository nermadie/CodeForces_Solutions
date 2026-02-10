# B. Hourglass
def solve(s, k, m):
    # s >= k
    if s >= k:
        remaining = m % k
        if (m // k) % 2 == 0:
            return s - remaining
        else:
            return k - remaining

    else:
        remaining = m % k
        return s - remaining if remaining <= s else 0


t = int(input())
for _ in range(t):
    s, k, m = map(int, input().split())
    print(solve(s, k, m))
