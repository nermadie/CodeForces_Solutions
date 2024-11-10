# B. Stalin Sort
def solve(n, a):
    sorted_a = sorted(a, reverse=True)
    cur_val = -1
    result = 2000
    for i in range(n):
        if sorted_a[i] != cur_val:
            cur_val = sorted_a[i]
            index = a.index(cur_val)
            result = min(result, index + i)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
