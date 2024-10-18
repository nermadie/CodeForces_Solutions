# A. Meaning Mean
def solve(n, a):
    a.sort()
    cur_val = a[0]
    for i in range(1, n):
        cur_val = (cur_val + a[i]) // 2
    return cur_val


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
