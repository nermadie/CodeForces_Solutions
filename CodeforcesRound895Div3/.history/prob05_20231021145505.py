# Data Structures Fan
def solve_test_case(n, a, s, q, query):
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    q = int(input())

    # Cal XOR of "0" arr and "1" arr
    xor_0 = 0
    xor_1 = 0
    for i in range(n):
        if s[i] == "0":
            xor_0 ^= a[i]
        else:
            xor_1 ^= a[i]

    for _ in range(q):
        query = list(map(int, input().split()))

    print(solve_test_case(n, a, s, q, query))
