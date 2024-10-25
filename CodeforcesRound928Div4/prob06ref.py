from itertools import combinations as q

e = range


def o(g, p):
    for i in e(1, 6):
        for j in e(1, 6):
            if (i + j) % 2 != p:
                continue
            if (
                g[i][j]
                + g[i - 1][j - 1]
                + g[i - 1][j + 1]
                + g[i + 1][j - 1]
                + g[i + 1][j + 1]
                == 5
            ):
                return 0
    return 1


def s():
    g = [[1 if c == "B" else 0 for c in input()] for _ in e(7)]
    a = [(i, j) for i in e(1, 6) for j in e(1, 6) if (i + j) % 2 == 0 and g[i][j]]
    b = [(i, j) for i in e(1, 6) for j in e(1, 6) if (i + j) % 2 == 1 and g[i][j]]

    def d(a, p):
        for k in e(len(a) + 1):
            for b in q(a, k):
                m = [r[:] for r in g]
                for i, j in b:
                    m[i][j] = 0
                if o(m, p):
                    return k

    print(d(a, 0) + d(b, 1))


for _ in e(int(input())):
    s()
