# Doremy's Drying Plan (Easy Version)
t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    range_dict = {}
    for i in range(m):
        left, right = list(map(int, input().split()))
        if range_dict.get(left) is not None:
            range_dict[left].append((i, right))
        else:
            range_dict[left] = [(i, right)]
        if range_dict.get(right) is not None:
            range_dict[right + 1].append((i, left))
        else:
            range_dict[right + 1] = [(i, left)]

    range_dict = dict(sorted(range_dict.items(), key=lambda x: x[0]))
