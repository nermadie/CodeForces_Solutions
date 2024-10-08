# The Corridor or There and Back Again
def max_k(n, traps):
    max_k_value = 1
    for trap in traps:
        if max_k_value < trap[0]:
            continue
        if trap[1] % 2 == 0:
            max_k_value = min(max_k_value, trap[0] + (trap[1] // 2) - 1)
        else:
            max_k_value = min(max_k_value, trap[0] + (trap[1] // 2))
    return max_k_value


t = int(input())

for _ in range(t):
    n = int(input())  # Number of traps
    traps = []
    for _ in range(n):
        di, si = map(int, input().split())
        traps.append((di, si))

    result = max_k(n, traps)
    print(result)
