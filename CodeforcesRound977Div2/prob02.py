# B. Maximize Mex
def solve(n, x, a):
    num_list = [0] * 200001
    for i in a:
        if i < n:
            num_list[i] += 1
    for i in range(n + 1):
        if num_list[i] == 0:
            return i
        else:
            if i + x <= n:
                num_list[i + x] += num_list[i] - 1


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, x, a))
