# C. Sakurako's Field Trip
def solve(n, a):
    result = 0
    limit = None
    if n % 2 == 0:
        limit = (n // 2) - 1
        if a[limit] == a[limit + 1]:
            result += 1
    else:
        limit = n // 2
    for i in range(limit):
        cur_same = 0
        if a[i] == a[i + 1]:
            cur_same += 1
        if a[n - i - 1] == a[n - i - 2]:
            cur_same += 1
        reversed_same = 0
        if a[i] == a[n - i - 2]:
            reversed_same += 1
        if a[i + 1] == a[n - i - 1]:
            reversed_same += 1
        result += min(cur_same, reversed_same)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
