# Money Trees
def max_subarray_length(n, k, a, h):
    # Handle h
    ok_subarr = []
    subarr = []
    for i in range(n - 1):
        if h[i] % h[i + 1] == 0:
            if len(subarr) <= 1:
                subarr.append(i)
            elif len(subarr) == 2:
                subarr[1] = i + 1
        else:
            if len(subarr) > 0:
                subarr.append(i)
                ok_subarr.append(subarr)
                subarr = []


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    result = max_subarray_length(n, k, a, h)
    print(result)
