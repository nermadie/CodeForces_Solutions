# A - Wallet Exchange
def solve(a, b):
    total = a + b
    if total % 2 == 0:
        return "Bob"
    else:
        return "Alice"


t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    print(solve(a, b))
