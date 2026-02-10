# A. DBMB and the Array
def solve(n, s, x, a):
    sum_a = sum(a)
    if sum_a > s:
        return "NO"
    if (s - sum_a) % x == 0:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, s, x, a))
