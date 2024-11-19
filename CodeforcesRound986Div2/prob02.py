# B. Alice's Adventures in Permuting
def solve(n, b, c):
    if n == 1:
        if c == 0:
            return 0
        else:
            return 1
    if b == 0:
        if n > c >= n - 2:
            return n - 1
        if c >= n:
            return n
        else:
            return -1
    num_small_than_n = 0
    temp_n = n
    if n <= b and n <= c:
        return n
    if n > c:
        num_small_than_n += 1
        temp_n -= c
        if temp_n >= b:
            num_small_than_n += temp_n // b
            if temp_n % b == 0:
                num_small_than_n -= 1

    return n - num_small_than_n


t = int(input())
for i in range(t):
    n, b, c = map(int, input().split())
    print(solve(n, b, c))
