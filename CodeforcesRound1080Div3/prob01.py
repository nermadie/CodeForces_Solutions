# A. Sieve of Erato67henes
def solve(n, a):
    return "YES" if 67 in a else "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
