# Parity Sort
def is_sortable_array(n, a):
    b = sorted(a)
    for i in range(n):
        if a[i] % 2 == 1 and b[i] % 2 == 0 or a[i] % 2 == 0 and b[i] % 2 == 1:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(is_sortable_array(n, a))
