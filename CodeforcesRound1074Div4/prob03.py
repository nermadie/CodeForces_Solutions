# C. Shifted MEX
def solve(n, a):
    a.sort()
    longest = 1
    prev = a[0]
    cnt = 1
    for i in range(1, n):
        if a[i] == prev:
            continue
        if a[i] == prev + 1:
            cnt += 1
            longest = max(longest, cnt)
        else:
            cnt = 1
        prev = a[i]
    longest = max(longest, cnt)
    return longest


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
