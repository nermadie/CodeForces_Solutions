# A. Sakurako and Kosuke
def solve(n):
    if n % 2 == 0:
        return "Sakurako"
    else:
        return "Kosuke"


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
