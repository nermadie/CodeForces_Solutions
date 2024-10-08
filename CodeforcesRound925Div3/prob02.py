# B. Make Equal
def can_equalize_water(n, containers):
    average = sum(containers) // n
    temp = 0
    for i in range(n-1, 0, -1):
        if containers[i] > average + temp:
            return "NO"
        else:
            temp += average - containers[i]
    return "YES"

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    containers = list(map(int, input().split()))
    print(can_equalize_water(n, containers))
