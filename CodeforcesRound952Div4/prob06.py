# F. Final Boss
from heapq import heappop, heappush


def solve(h, n, a, c):
    first_phase_damage = 0
    queue = []
    for i in range(n):
        first_phase_damage += a[i]
        heappush(queue, (c[i], i))

    h -= first_phase_damage
    x = 0
    while True:
        if h <= 0:
            return x + 1
        x, i = heappop(queue)
        h -= a[i]
        heappush(queue, (c[i] + x, i))


t = int(input())
for _ in range(t):
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(solve(h, n, a, c))
