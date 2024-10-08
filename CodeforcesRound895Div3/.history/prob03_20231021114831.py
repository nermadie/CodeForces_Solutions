# Non-coprime Split
def find_a_and_b(l, r):
    if l % 2 == 0:
        return l, l - 1
    if r % 2 == 0:
        return r, r - 1
    return -1, -1


t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    a, b = find_a_and_b(l, r)
    print(a, b)
