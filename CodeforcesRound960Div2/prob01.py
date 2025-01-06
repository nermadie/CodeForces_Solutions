# A. Submission Bait
def solve(n, a):
    dict_a = {}
    for item in a:
        dict_a.setdefault(item, 0)
        dict_a[item] += 1
    list_dict_a = list(dict_a.items())
    list_dict_a.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(list_dict_a)):
        if list_dict_a[i][1] % 2 == 1:
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
