# E. Beautiful Array
def solve(n, k, a):
    k_remainder = {}
    odd_count = 0
    for i in range(n):
        cur_remainder = a[i] % k
        k_remainder.setdefault(cur_remainder, []).append(a[i])
        if len(k_remainder[cur_remainder]) % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1
    if odd_count != n % 2:
        return -1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
