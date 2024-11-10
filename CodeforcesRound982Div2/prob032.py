# C. Add Zeros
def solve(n, a):
    if n == 1:
        return 1
    require_length = []
    for i in range(n):
        require_length.append(a[i] + i)
    require_length_sorted = sorted(enumerate(require_length), key=lambda x: x[1])
    appeared_set = set()
    appeared_set.add(n)
    result = n
    for i in range(n):
        if require_length_sorted[i][1] >= n * n:
            continue
        if require_length_sorted[i][1] in appeared_set:
            result = max(
                result, require_length_sorted[i][1] + require_length_sorted[i][0]
            )
            appeared_set.add(require_length_sorted[i][1] + require_length_sorted[i][0])
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
