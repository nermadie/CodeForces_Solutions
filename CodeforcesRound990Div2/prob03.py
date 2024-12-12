# C. Swap Columns and Find a Path
def solve(n, a1, a2):
    max_remain = -100000
    result = 0
    for i in range(n):
        if a1[i] > a2[i]:
            result += a1[i]
            max_remain = max(max_remain, a2[i])
        else:
            result += a2[i]
            max_remain = max(max_remain, a1[i])
    return result + max_remain


t = int(input())
for _ in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    print(solve(n, a1, a2))
