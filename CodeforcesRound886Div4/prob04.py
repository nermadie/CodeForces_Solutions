# Balanced Round
def min_problems_to_remove(n, k, difficulties):
    difficulties.sort()
    max_len = 1
    count = 1
    for i in range(n - 1):
        if difficulties[i + 1] - difficulties[i] <= k:
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 1
    return n - max_len


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    result = min_problems_to_remove(n, k, a)
    print(result)
