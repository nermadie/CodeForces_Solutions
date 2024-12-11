# B. Everyone Loves Tres
def solve(n):
    if n % 2 == 1 and n > 4:
        return int((n - 4) * "3" + "6366")
    elif n % 2 == 0:
        return int((n - 2) * "3" + "66")
    else:
        return -1


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
