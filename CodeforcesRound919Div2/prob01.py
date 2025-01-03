# A. Satisfying Constraints
def solve(n, ax):
    lower_bound = 0
    upper_bound = 10**9
    diff = set()
    for a, x in ax:
        if a == 1:
            lower_bound = max(lower_bound, x)
        elif a == 2:
            upper_bound = min(upper_bound, x)
        elif a == 3:
            diff.add(x)
    diff_outside = 0
    for i in diff:
        if i < lower_bound or i > upper_bound:
            diff_outside += 1
    result = upper_bound - lower_bound + 1 + diff_outside - len(diff)
    return result if result > 0 else 0


t = int(input())
for _ in range(t):
    n = int(input())
    ax = []
    for _ in range(n):
        ax.append(list(map(int, input().split())))
    print(solve(n, ax))
