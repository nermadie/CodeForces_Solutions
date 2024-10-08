# E. Triple Operations
def solve(l, r):
    cur_left = l
    first_l = l
    count = 0
    while first_l != 0:
        first_l //= 3
        count += 1
    result = count
    while 3**count <= r:
        result += (3**count - cur_left) * count
        cur_left = 3**count
        count += 1
    result += (r - cur_left + 1) * count
    return result


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(solve(l, r))
