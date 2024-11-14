# A. Bus to Pénjamo
def solve(n, r, a):
    persons = sum(a)
    able_alone_seats = r * 2 - persons if persons > r else persons
    result = 0
    for i in range(n):
        if a[i] % 2 == 1:
            if able_alone_seats > 0:
                able_alone_seats -= 1
                result += 1
            a[i] -= 1
        result += a[i]
    return result


t = int(input())
for _ in range(t):
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, r, a))
