# Money Trees
def max_subarray_length(n, k, a, h):
    # Handle h

    for i in range(n-1):
        if h[i] % h[i+1] == 0:


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    result = max_subarray_length(n, k, a, h)
    print(result)
