# D. Vlad and Division
def solve(n, a):
    count_pair = 0
    checked_dict = {}
    for i in range(n):
        checked_dict.setdefault(a[i], 0)
        checked_dict.setdefault(a[i] ^ ((1 << 31) - 1), 0)
        if checked_dict[a[i]] > 0:
            count_pair += 1
            checked_dict[a[i]] -= 1
        else:
            checked_dict[a[i] ^ ((1 << 31) - 1)] += 1
    return n - count_pair


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
