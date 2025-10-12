# A. Diagonals
def solve(n, k):
    if k == 0:
        return 0
    if n >= k:
        return 1
    result = 1
    k -= n
    for i in range(n - 1, 0, -1):
        result += 1
        if i >= k:
            return result
        else:
            k -= i
        result += 1
        if i >= k:
            return result
        else:
            k -= i
    return 2 * n - 1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
