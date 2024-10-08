# C. Update Queries
def solve(n, m, s, ind, c):
    s = list(s)
    c_list = list(c)
    c_list.sort()
    ind.sort()
    ind_set = set(ind)
    ind_list = sorted(list(ind_set))
    for i in range(len(ind_list)):
        s[ind_list[i] - 1] = c_list[i]
    return "".join(s)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    ind = list(map(int, input().split()))
    c = input()
    print(solve(n, m, s, ind, c))
