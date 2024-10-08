# A. Dora's Set
def solve(l, r):
    num_odd = 0
    if l % 2 == 0 and r % 2 == 0:
        num_odd = (r - l + 1) // 2
    elif l % 2 == 1 and r % 2 == 1:
        num_odd = (r - l + 1) // 2 + 1
    else:
        num_odd = (r - l + 1) // 2
    return num_odd // 2


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(solve(l, r))
