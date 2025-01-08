# B. Removals Game
def solve(n, a, b):
    b_reversed = b[::-1]
    check1 = True
    check2 = True
    for i in range(n):
        if a[i] != b[i]:
            check1 = False
        if a[i] != b_reversed[i]:
            check2 = False
        if not check1 and not check2:
            return "Alice"
    return "Bob"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
