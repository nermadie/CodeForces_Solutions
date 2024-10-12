# D. Permutation Game
def find_max(n, k, pos, p, a):
    total = 0
    cur_max = 0
    for i in range(min(k, n)):
        cur_max = max(total + a[pos - 1] * (k - i), cur_max)
        total += a[pos - 1]
        if pos == p[pos - 1]:
            return cur_max
        pos = p[pos - 1]
    return cur_max


def solve(n, k, pb, ps, p, a):
    Bodya = find_max(n, k, pb, p, a)
    Sasha = find_max(n, k, ps, p, a)
    if Bodya > Sasha:
        return "Bodya"
    elif Sasha > Bodya:
        return "Sasha"
    else:
        return "Draw"


t = int(input())
for _ in range(t):
    n, k, pb, ps = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(solve(n, k, pb, ps, p, a))
