# B. Seating in a Bus
def solve(n, a):
    if n == 1:
        return "YES"
    must_choose_set = set()
    must_choose_set.add(a[0])
    must_choose_set.add(a[0] + 1)
    must_choose_set.add(a[0] - 1)
    for i in range(1, n):
        if a[i] in must_choose_set:
            must_choose_set.add(a[i] + 1)
            must_choose_set.add(a[i] - 1)
        else:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
