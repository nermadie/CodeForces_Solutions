# F. Kosuke's Sloth
def solve(n, k):
    a, b = 0, 1 % k
    index = 1
    while b:
        a, b = b, (a + b) % k
        index += 1
    return (index * n) % (10**9 + 7)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
