# Data Structures Fan
from operator import xor

XOR_0 = 0
XOR_1 = 0
XOR_ALL = [0] * 1000000


def solve_test_case(n, a, s, q, query, xor_0, xor_1, xor_all):
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    q = int(input())

    # Cal XOR of "0" arr and "1" arr
    for i in range(n):
        if s[i] == "0":
            XOR_0 ^= a[i]
        else:
            XOR_1 ^= a[i]
    # Cal for all XOR from 1 to n
    xor_all = [0] * n
    xor_all[0] = a[0]
    for i in range(1, n):
        xor_all[i] = xor_all[i - 1] ^ a[i]

    for _ in range(q):
        query = list(map(int, input().split()))
        print(solve_test_case(n, a, s, q, query, xor_0, xor_1, xor_all))