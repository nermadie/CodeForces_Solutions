# A. Marisa Steals Reimu's Takeout
def solve(n, w):
    k_0 = []
    k_1 = []
    k_2 = []
    for item in w:
        if item % 3 == 0:
            k_0.append(item)
        elif item % 3 == 1:
            k_1.append(item)
        else:
            k_2.append(item)

    min_k1_k2 = min(len(k_1), len(k_2))
    max_k1_k2 = max(len(k_1), len(k_2))

    return len(k_0) + min_k1_k2 + (max_k1_k2 - min_k1_k2) // 3


t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    print(solve(n, w))
