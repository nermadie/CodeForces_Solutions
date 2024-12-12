# B. All Pairs Segments
def solve(n, q, x, k):
    result_dict = {}
    for i in range(n - 1):
        result_dict.setdefault((n - i - 1) * (i + 1), 0)
        result_dict[(n - i - 1) * (i + 1)] += x[i + 1] - x[i] - 1
        result_dict.setdefault((i + 1) * (n - i) - 1, 0)
        result_dict[(i + 1) * (n - i) - 1] += 1
    result_dict[n - 1] += 1
    result = []
    for query in k:
        if query in result_dict:
            result.append(result_dict[query])
        else:
            result.append(0)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    k = list(map(int, input().split()))
    print(solve(n, q, x, k))
