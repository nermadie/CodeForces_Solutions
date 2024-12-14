# B. Minimize Equal Sum Subarrays
def solve(n, p):
    result = []
    for i in p:
        result.append((i % n) + 1)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    arr = solve(n, p)
    print(" ".join(map(str, arr)))
