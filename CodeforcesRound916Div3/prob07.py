# F. Programming Competition
def solve(n, p):
    direct = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        direct[p[i]].append(i + 2)
    cur_level = [1]
    len_level = [0] * n
    for i in range(n):
        len_level[i] = len(cur_level)
        next_level = []
        for level in cur_level:
            next_level.extend(direct[level])
        cur_level = next_level
    result, remain_alone = 0, 0
    for i in range(n):
        if len_level[i] + remain_alone > 1:
            result += 1
            remain_alone += len_level[i] - 2
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
