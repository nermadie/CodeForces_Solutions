# B. Parity and Sum
def solve(n, a):
    odd = []
    even = []
    for item in a:
        if item % 2 == 1:
            odd.append(item)
        else:
            even.append(item)
    odd.sort()
    even.sort()
    if len(odd) == 0:
        return 0
    last_odd = odd[-1]
    result = 0
    for item in even:
        if last_odd > item:
            result += 1
            last_odd += item
        else:
            return len(even) + 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
