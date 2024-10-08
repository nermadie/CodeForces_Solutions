# Data Structures Fan
from operator import xor

XOR_0 = 0
XOR_1 = 0
XOR_ALL = [0] * 100000


def solve_test_case(n, a, s, q, query):
    global XOR_0, XOR_1, XOR_ALL
    if query[0] == 1:
        # XOR tu a[l] den a[r] ~ XOR_ALL[r] ^ XOR_ALL[l-1]
        xor_l_r = XOR_ALL[query[2] - 1] ^ XOR_ALL[query[1] - 2]
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

    for _ in range(q):
        query = list(map(int, input().split()))
        solve_test_case(n, a, s, q, query)
    print()
