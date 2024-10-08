# A. Robin Helps
def solve(n, k, a):
    cur_gold = 0
    result = 0
    for item in a:
        if item >= k:
            cur_gold += item
        elif item == 0 and cur_gold > 0:
            cur_gold -= 1
            result += 1
    return result


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
