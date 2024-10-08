# Assembly via Minimums
def restore_array(n, b):
    b.sort()
    result = [b[0]]
    count = 0
    cur_n = n - 1
    for i in range(1, len(b)):
        count += 1
        if count == cur_n:
            result.append(b[i])
            cur_n -= 1
            count = 0
    result.append(b[-1])
    return result


t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    result = restore_array(n, b)
    print(" ".join(map(str, result)))
