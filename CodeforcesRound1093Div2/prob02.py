# B. OIE Excursion
def solve(m, n, a):
    count_same = 1
    for i in range(1, m):
        if a[i] == a[i - 1]:
            count_same += 1
        else:
            count_same = 1
        if count_same >= n:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(m, n, a))
