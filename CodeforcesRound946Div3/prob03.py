# C. Beautiful Triple Pairs
def solve(n, a):
    result = 0
    dict_template = {}
    for i in range(n - 2):
        template = [0] * 3
        template[0] = (0, a[i + 1], a[i + 2])
        template[1] = (a[i], 0, a[i + 2])
        template[2] = (a[i], a[i + 1], 0)
        same_template = (a[i], a[i + 1], a[i + 2])
        for temp in template:
            dict_template.setdefault(temp, 0)
            result += dict_template[temp]
            dict_template[temp] += 1
        result -= dict_template.get(same_template, 0) * 3
        dict_template.setdefault(same_template, 0)
        dict_template[same_template] += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
