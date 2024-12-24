# B. Paint a Strip
def solve(n):
    if n == 1:
        return 1
    result = 1
    cur_bound = 1
    while n > cur_bound:
        cur_bound = (cur_bound + 1) * 2
        result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
