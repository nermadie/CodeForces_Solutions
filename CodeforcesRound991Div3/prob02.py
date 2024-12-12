# B. Transfusion
def solve(n, a):
    odd = 0
    even = 0
    for i in range(n):
        if i % 2 == 0:
            odd += a[i]
        else:
            even += a[i]
    n_odd = n // 2
    n_even = n // 2
    if n % 2 == 1:
        n_odd += 1
    if (odd / n_odd).is_integer() and (even / n_even).is_integer():
        if odd // n_odd == even // n_even:
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
