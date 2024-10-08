# Data Structures Fan
from operator import xor

XOR_0 = 0
XOR_1 = 0
XOR_ALL = [0] * 100000


def solve_test_case(n, a, s, q, query):
    global XOR_0, XOR_1, XOR_ALL
    result = ""
    if query[0] == 1:
        # XOR tu a[l] den a[r] ~ XOR_ALL[r] ^ XOR_ALL[l-1]
        xor_l_r = XOR_ALL[query[2] - 1] ^ XOR_ALL[query[1] - 2]
        XOR_0 ^= xor_l_r
        XOR_1 ^= xor_l_r
    if query[0] == 2:
        if query[1] == 0:
            result += str(XOR_0) + " "
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
    XOR_ALL[0] = a[0]
    for i in range(1, n):
        XOR_ALL[i] = XOR_ALL[i - 1] ^ a[i]

    for _ in range(q):
        query = list(map(int, input().split()))
        print(solve_test_case(n, a, s, q, query))
    print()