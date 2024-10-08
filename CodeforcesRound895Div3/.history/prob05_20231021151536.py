# Data Structures Fan
from operator import xor

XOR_0 = 0
XOR_1 = 0
XOR_ALL = None


def solve_test_case(n, a, s, q, query):
    global XOR_0, XOR_1, XOR_ALL
    if query[0] == 1:
        # XOR tu a[l] den a[r] ~ XOR_ALL[r] ^ XOR_ALL[l-1]
        xor_l_r = XOR_ALL[query[2]] ^ XOR_ALL[query[1] - 1]
        XOR_0 ^= xor_l_r
        XOR_1 ^= xor_l_r
    if query[0] == 2:
        if query[1] == 0:
            print(XOR_0, end=" ")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    q = int(input())

    # Cal XOR of "0" arr and "1" arr
    # Cal for all XOR from 1 to n
    XOR_ALL = [0] * (n + 1)
    for i in range(n):
        XOR_ALL[i] = XOR_ALL[i - 1] ^ a[i]
        if s[i] == "0":
            XOR_0 ^= a[i]
        else:
            XOR_1 ^= a[i]
    XOR_ALL[0] = a[0]
    for _ in range(q):
        query = list(map(int, input().split()))
        solve_test_case(n, a, s, q, query)
    print()
