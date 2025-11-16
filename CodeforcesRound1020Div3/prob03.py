# C. Cherry Bomb
def solve(n, k, a, b):
    check_sum = -1
    for i in range(n):
        if b[i] == -1:
            continue
        if check_sum != -1:
            if a[i] + b[i] != check_sum:
                return 0
        check_sum = a[i] + b[i]
    if check_sum != -1:
        if max(a) > check_sum or min(a) + k < check_sum:
            return 0
        else:
            return 1
    return k - (max(a) - min(a)) + 1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, k, a, b))
