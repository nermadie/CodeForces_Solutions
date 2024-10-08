# Non-coprime Split
def find_a_and_b(l, r):
    if r <= 3:
        return -1
    if r % 2 == 0:
        return r // 2, r // 2
    elif r % 2 == 1:
        return (r - 1) // 2, (r + 1) // 2
    return -1


t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    a, b = find_a_and_b(l, r)
    print(a, b)
