# B. Chaya Calendar
def solve(n, a):
    cur_year = 0
    for item in a:
        prev = (cur_year - 1) // item
        cur_year = item * prev
    return -cur_year


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
