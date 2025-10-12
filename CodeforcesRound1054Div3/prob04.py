# D. A and B
def cost(c: str) -> int:
    pos = [i for i, ch in enumerate(s) if ch == c]
    k = len(pos)
    if k <= 1:
        return 0

    q = [pos[i] - i for i in range(k)]
    med = q[k // 2]
    return sum(abs(x - med) for x in q)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    print(min(cost('a'), cost('b')))