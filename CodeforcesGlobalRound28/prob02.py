# B. Kevin and Permutation
def solve(n, k):
    result = []
    cur_nor_val = n // k + 1
    cur_min_val = 1
    for i in range(1, n + 1):
        if i % k == 0:
            result.append(cur_min_val)
            cur_min_val += 1
        else:
            result.append(cur_nor_val)
            cur_nor_val += 1
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
