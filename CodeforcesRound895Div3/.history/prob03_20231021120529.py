# Non-coprime Split
def find_a_and_b(l, r):
    if r <= 3:
        return -1, -1
    if r % 2 == 0:
        return r // 2, r // 2
    elif r % 2 == 1 and r != l:
        return (r - 1) // 2, (r - 1) // 2
    else:  # r == l and r % 2 == 1
        for i in range(3, l // 2):
            if (r - i) % i == 0:
                return i, r - i
    return -1, -1


t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    a, b = find_a_and_b(l, r)
    print(a, b)
