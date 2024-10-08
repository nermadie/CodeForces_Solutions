# Increasing Sequence
def minimum_bn_value(n, a):
    cur_bi = 0
    count = 0
    while True:
        if count == n:
            break
        if a[count] == cur_bi + 1:
            cur_bi += 2
            count += 1
        else:
            cur_bi += 1
            count += 1
    return cur_bi


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(minimum_bn_value(n, a))
