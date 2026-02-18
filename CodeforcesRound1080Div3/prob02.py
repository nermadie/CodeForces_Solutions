# B. Heapify 1
def solve(n, a):
    if n <= 2:
        return "YES"
    check_range = n // 2 + 1 if n % 2 != 0 else n // 2
    for i in range(check_range):
        i_mul = i + 1
        check = False
        while i_mul - 1 < n:
            if a[i_mul - 1] != i + 1:
                i_mul *= 2
            else:
                check = True
                temp = a[i]
                a[i] = a[i_mul - 1]
                a[i_mul - 1] = temp
                break
        if not check:
            return "NO"
    for i in range(n):
        if a[i] != i + 1:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
