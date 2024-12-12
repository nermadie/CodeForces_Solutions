# A. Line Breaks
def solve(n, m, s):
    cur_len = 0
    result = 0
    for i in range(n):
        if len(s[i]) + cur_len <= m:
            cur_len += len(s[i])
            result += 1
        else:
            return result
    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    print(solve(n, m, s))
