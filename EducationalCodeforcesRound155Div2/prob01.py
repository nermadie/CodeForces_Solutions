# Rigged!
def solve(n, athletes):
    polycarp_s = athletes[0][0]
    polycarp_e = athletes[0][1]
    for i in range(1, n):
        if athletes[i][0] >= polycarp_s:
            if athletes[i][1] >= polycarp_e:
                return -1
    return polycarp_s


t = int(input())

for _ in range(t):
    n = int(input())
    athletes = []
    for _ in range(n):
        s, e = map(int, input().split())
        athletes.append((s, e))
    print(solve(n, athletes))
