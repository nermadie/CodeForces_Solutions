# D. Find the Different Ones!
def solve(n, a, q, lr):
    prev_group_index = [None] * n
    cur_group = a[0]
    prev_group_last_index = -1
    for i in range(n):
        if a[i] != cur_group:
            prev_group_last_index = i - 1
            cur_group = a[i]
        prev_group_index[i] = prev_group_last_index
    for l, r in lr:
        if a[l - 1] != a[r - 1]:
            print(l, r)
        else:
            if prev_group_index[r - 1] >= l - 1:
                print(prev_group_index[r - 1] + 1, r)
            else:
                print("-1 -1")
    print()


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    lr = []
    for _ in range(q):
        l, r = map(int, input().split())
        lr.append((l, r))
    solve(n, a, q, lr)
