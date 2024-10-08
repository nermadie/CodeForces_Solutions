# B. Angry Monk
def solve(n, k, a):
    max_a = max(a)
    a.remove(max_a)
    result = 0
    for item in a:
        result += item + item - 1
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
