# A. Social Experiment
def solve(n):
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n % 2 == 0:
        return 0
    return 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))