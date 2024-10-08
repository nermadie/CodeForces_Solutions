# Sequence Game
import io, os, sys


def find_sequence_a(n, b):
    i = 0
    result = [0] * 400000
    result[0] = b[0]
    result_index = 1
    for i in range(1, n):
        if b[i] >= b[i - 1]:
            result[result_index] = b[i]
            result_index += 1
        else:
            result[result_index] = 1
            result[result_index + 1] = b[i]
            result_index += 2
    return result_index, result[:result_index]


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input().decode())

for _ in range(t):
    n = int(input().decode())
    b = list(map(int, input().decode().split()))

    m, a = find_sequence_a(n, b)

    sys.stdout.write(str(m) + "\n")
    sys.stdout.write(" ".join(map(str, a)) + "\n")
