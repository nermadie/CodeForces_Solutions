# Data Structures Fan
def solve_test_case(n, a, s, q, query):
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    q = int(input())

    for _ in range(q):
        query = list(map(int, input().split()))

    print(solve_test_case(n, a, s, q, query))
