import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    l = input().split()
    l1 = []
    for i in range(n):
        l1.append((int(l[i]), i))
    heapq.heapify(l1)
    c = -1
    ans = []
    while len(l1) > 0:
        a, b = heapq.heappop(l1)
        if b > c:
            c = b
            ans.append(a)
        else:
            heapq.heappush(l1, (a + 1, n))
            n += 1
    print(" ".join(map(str, ans)))
