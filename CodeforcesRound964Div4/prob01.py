# A. A+B Again?
def solve(n):
    return int(n[0]) + int(n[1])


t = int(input())
for _ in range(t):
    n = input()
    print(solve(n))
