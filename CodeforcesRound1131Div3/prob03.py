# C. Math and Physics
def solve(n, a):
    is_all_1 = True
    is_all_mid_1 = True
    for i in range(0, n):
        if a[i] != 1:
            is_all_1 = False
        if a[i] != 1 and i != 0 and i != n - 1:
            is_all_mid_1 = False
    if is_all_1:
        return -1
    total = sum(a)
    if is_all_mid_1:
        total -= n - 1
    else:
        total -= 1
    return total


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
