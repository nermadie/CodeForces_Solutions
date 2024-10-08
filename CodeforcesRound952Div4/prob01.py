# A. Creating Words
def solve(a, b):
    first_a = a[0]
    first_b = b[0]
    a = first_b + a[1:]
    b = first_a + b[1:]
    return a + " " + b


t = int(input())
for _ in range(t):
    a, b = input().split()
    print(solve(a, b))
