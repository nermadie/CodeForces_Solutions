# D. Kousuke's Assignment
def solve(n, p):
    sum_list = [0] * (n + 1)
    for i in range(n):
        sum_list[i + 1] = sum_list[i] + p[i]
    queue = set()
    result = 0
    for i in range(n + 1):
        if sum_list[i] not in queue:
            queue.add(sum_list[i])
        else:
            result += 1
            queue = {sum_list[i]}
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
