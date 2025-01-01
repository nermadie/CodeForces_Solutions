# B. Game with Colored Marbles
def solve(n, c):
    dict_count = {}
    for i in c:
        dict_count.setdefault(i, 0)
        dict_count[i] += 1
    list_count = list(dict_count.values())
    result = 0
    for value in list_count:
        if value == 1:
            result += 1
    remain = len(list_count) - result
    result = (result + 1) // 2
    return remain + result * 2


t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    print(solve(n, c))
