# B. Game with Doors
def solve(l, r, L, R):
    if r < L or R < l:
        return 1
    else:
        result = 0
        if R > r:
            if l < L:
                result = r - L + 2
            else:
                result = r - l + 2
        else:
            if l < L:
                result = R - L + 2
            else:
                result = R - l + 2
        if l == L:
            result -= 1
        if r == R:
            result -= 1
        return result


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    print(solve(l, r, L, R))
