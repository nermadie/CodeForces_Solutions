# Money Trees
def max_subarray_length(n, k, a, h):
    max_length = 0
    current_length = 1
    current_height = h[0]

    for i in range(1, n):
        if current_height % h[i] == 0:
            current_length += 1
        else:
            current_length = 1
        current_height = h[i]

        if current_length > max_length and sum(a[i - current_length + 1 : i + 1]) <= k:
            max_length = current_length

    return 0


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    result = max_subarray_length(n, k, a, h)
    print(result)
