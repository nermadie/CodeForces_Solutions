# A. Make All Equal
def solve(n, a):
    appear_dict = {}
    for i in a:
        appear_dict.setdefault(i, 0)
        appear_dict[i] += 1
    appear_list = list(appear_dict.items())
    appear_list.sort(key=lambda x: x[1])
    return n - appear_list[-1][1]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
