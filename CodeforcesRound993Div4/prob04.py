# D. Harder Problem
def solve(n, a):
    a_check = [False] * (n + 1)
    a_set = set()
    for i in a:
        a_set.add(i)
        a_check[i] = True
    result = list(a_set)
    for i in range(1, n + 1):
        if not a_check[i]:
            result.append(i)
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    print(solve(n, a))
