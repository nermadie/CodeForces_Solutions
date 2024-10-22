# E. Klever Permutation
def solve(n, k):
    result = [0] * n
    check_increasing = True
    cur_val = 1
    for i in range(k):
        if check_increasing:
            for pos in range(i, n, k):
                result[pos] = cur_val
                cur_val += 1
            check_increasing = False
        else:
            for pos in range((n // k) * k + i, -1, -k):
                if pos >= n:
                    continue
                result[pos] = cur_val
                cur_val += 1
            check_increasing = True
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
