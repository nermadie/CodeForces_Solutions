def solve(n, k, a):
    cur_k = k
    result = 0
    i = 0
    while i < n:
        if a[i] == 0:
            cur_k -= 1
            if cur_k == 0:
                result += 1
                i += 1
                cur_k = k
        else:
            cur_k = k
        i += 1

    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
