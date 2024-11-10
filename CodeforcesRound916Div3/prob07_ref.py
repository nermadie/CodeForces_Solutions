for j in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    L = [0] * n
    T = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        T[A[i - 2]].append(i)
    q = [(1, 0)]
    while q:
        v, l = q.pop()
        L[l] += 1
        for u in T[v]:
            q.append((u, l + 1))
    ans, sm = 0, 0
    for i in range(n):
        if L[i] + sm > 1:
            ans += 1
            sm += L[i] - 2
    print(ans)
