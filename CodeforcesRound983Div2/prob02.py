# B. Medians
def solve(n, k):
    if n == 1:
        print(1)
        print(1)
        return
    if k == 1 or k == n:
        print(-1)
        return
    left = 1
    middle = (n // 2) + 1
    total_left = k - 1
    total_right = n - k
    diff = abs(total_left - total_right)
    result = []
    if k > middle:
        print(2 * total_right + 1)
        result.append(left)
        left += 1 + diff
        for _ in range(left, k):
            result.append(left)
            left += 1
        result.append(left)
        left += 1
        for _ in range(total_right):
            result.append(left)
            left += 1
    elif k < middle:
        print(2 * total_left + 1)
        for _ in range(total_left):
            result.append(left)
            left += 1
        result.append(left)
        left += 1
        result.append(left)
        left += 1 + diff
        for _ in range(left, n + 1):
            result.append(left)
            left += 1
    else:
        print(n)
        for i in range(1, n + 1):
            result.append(i)
    print(*result)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
