# B1. The Strict Teacher (Hard Version)
def solve(n, m, q, b, a):
    b.sort()
    a_enu = list(enumerate(a))
    a_enu.sort(key=lambda x: x[1])
    a_index = 0
    result = []
    while a_index < q and b[0] > a_enu[a_index][1]:
        result.append((a_enu[a_index][0], b[0] - 1))
        a_index += 1
    for i in range(m - 1):
        while a_index < q and b[i] < a_enu[a_index][1] < b[i + 1]:
            result.append((a_enu[a_index][0], (b[i + 1] - b[i]) // 2))
            a_index += 1
    while a_index < q and a_enu[a_index][1] > b[-1]:
        result.append((a_enu[a_index][0], n - b[-1]))
        a_index += 1
    result.sort(lambda item: item[0])
    for item in result:
        print(item[1])


t = int(input())
for _ in range(t):
    n, m, q = map(int, input().split())
    b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    solve(n, m, q, b, a)
