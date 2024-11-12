# A. Circuit
def solve(n, a):
    count_1 = a.count(1)
    count_0 = 2 * n - count_1
    if count_1 % 2 == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")
    if count_0 > n:
        print(2 * n - count_0)
    else:
        print(count_0)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)
