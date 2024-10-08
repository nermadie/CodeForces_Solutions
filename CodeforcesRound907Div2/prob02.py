# Deja Vu
import io, os, sys


def apply_modifications(n, arr, queries):
    divisor_arr = [0] * len(arr)
    for i in range(len(arr)):
        count = 1
        pow_res = 2
        while arr[i] % pow_res == 0:
            count += 1
            pow_res *= 2
        divisor_arr[i] = count - 1
    cur = 30
    for i in range(len(queries)):
        if queries[i] > cur:
            continue
        for j in range(len(arr)):
            if divisor_arr[j] >= queries[i]:
                arr[j] += pow(2, queries[i] - 1)
                divisor_arr[j] = queries[i] - 1
                cur = queries[i] - 1
    return arr


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input().decode())


for _ in range(t):
    n, q = map(int, input().decode().split())
    arr = list(map(int, input().decode().split()))
    queries = list(map(int, input().decode().split()))

    sys.stdout.write(" ".join(map(str, apply_modifications(n, arr, queries))) + "\n")
