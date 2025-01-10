# A. MEX Destruction
def solve(n, a):
    first_diff0_index = -1
    last_diff0_index = -1
    for i in range(n):
        if a[i] != 0:
            first_diff0_index = i
            break
    for i in range(n - 1, -1, -1):
        if a[i] != 0:
            last_diff0_index = i
            break
    if first_diff0_index == -1 and last_diff0_index == -1:
        return 0
    middle = a[first_diff0_index : last_diff0_index + 1]
    result = 0
    if 0 in middle:
        result += 2
    if first_diff0_index != -1 or last_diff0_index != -1:
        result += 1
    return result if result <= 2 else 2


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
