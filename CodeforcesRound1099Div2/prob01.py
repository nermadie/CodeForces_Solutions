# A. Construct an Array
def solve(n):
    result = [x for x in range(1, 2 * n, 2)]
    return " ".join(map(str, result))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
