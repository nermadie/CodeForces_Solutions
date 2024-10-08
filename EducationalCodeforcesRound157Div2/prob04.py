# XOR Construction
def construct_array(n, a):
    b = [0] * n
    for i in range(n):
        b[0] = i
        check = True
        for j in range(1, n):
            b[j] = a[j - 1] ^ b[j - 1]
            if b[j] >= n:
                check = False
                break
        if check:
            return b


n = int(input())
a = list(map(int, input().split()))

result = construct_array(n, a)

print(*result)
