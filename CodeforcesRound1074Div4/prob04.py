# D. OutOfMemoryError
def solve(n, m, h, a, operations):
    changes = []
    a_clone = a.copy()
    for i in range(m):
        b, c = operations[i]
        changes.append(b - 1)
        if a[b - 1] + c > h:
            while len(changes) > 0:
                idx = changes.pop()
                a[idx] = a_clone[idx]
        else:
            a[b - 1] += c
    return " ".join(map(str, a))


t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    a = list(map(int, input().split()))
    operations = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, h, a, operations))
