# A. Problem Generator
def solve(n, m, a):
    prob_diff_dict = {}
    for i in range(n):
        prob_diff_dict.setdefault(a[i], 0)
        prob_diff_dict[a[i]] += 1
    result = 0
    for prob_diff, count in prob_diff_dict.items():
        if count < m:
            result += m - count
    result += (7 - len(prob_diff_dict)) * m
    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    print(solve(n, m, a))
