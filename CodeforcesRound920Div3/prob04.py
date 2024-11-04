# D. Very Different Array
def solve(n, m, a, b):
    a.sort()
    b.sort(reverse=True)
    temp_result = 0
    for i in range(n):
        temp_result += abs(a[i] - b[i])
    result = temp_result
    for i in range(n - 1, -1, -1):
        temp_result = temp_result - abs(a[i] - b[i]) + abs(a[i] - b[m - (n - i)])
        result = max(result, temp_result)

    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, a, b))
