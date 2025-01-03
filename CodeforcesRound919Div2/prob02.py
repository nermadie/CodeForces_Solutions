# B. Summation Game
def solve(n, k, x, a):
    a.sort()
    sum_a_list = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_a_list[i] = sum_a_list[i - 1] + a[i - 1]
    result = sum_a_list[n] - 2 * (sum_a_list[n] - sum_a_list[n - x])
    for i in range(k):
        if n - i - 1 >= x:
            result = max(
                result,
                sum_a_list[n - i - 1]
                - 2 * (sum_a_list[n - i - 1] - sum_a_list[n - i - 1 - x]),
            )
        else:
            result = max(result, -sum_a_list[n - k])
            break
    return result


t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, x, a))
